import os
import glob
import itertools
import time
import httpx
from openai import OpenAI, BadRequestError
from datetime import datetime
from typing import Optional, List, Dict, Any
import streamlit as st

class VectorStoreManager:
    """Manages OpenAI Vector Store operations"""
    
    def __init__(self, api_key: str, cli_mode: bool = False):
        """Initialize with OpenAI API key"""
        self.client = OpenAI(api_key=api_key)
        self.api_key = api_key
        self.cli_mode = cli_mode
    
    def _log(self, message: str, level: str = "info"):
        """Log message using appropriate method based on context"""
        if self.cli_mode:
            # CLI mode - use print statements
            if level == "success":
                print(f"✅ {message}")
            elif level == "warning":
                print(f"⚠️  {message}")
            elif level == "error":
                print(f"❌ {message}")
            else:
                print(f"ℹ️  {message}")
        else:
            # Streamlit mode - use st functions
            if level == "success":
                st.success(message)
            elif level == "warning":
                st.warning(message)
            elif level == "error":
                st.error(message)
            else:
                st.info(message)
    
    def get_or_create_vector_store(self, name: str) -> str:
        """
        Retrieves an existing vector store by name or creates a new one.
        Returns the vector_store_id.
        """
        stores = self.client.vector_stores.list()
        for store in stores.data:
            if store.name == name:
                self._log(f"Found existing vector store '{name}' (id={store.id})", "success")
                return store.id
        
        vs = self.client.vector_stores.create(name=name)
        self._log(f"Created new vector store '{name}' (id={vs.id})", "success")
        return vs.id
    
    def upload_to_vector_store(
        self,
        dir_path: str,
        vector_store_id: str,
        extensions: tuple[str, ...] = ("pdf", "md", "markdown", "txt"),
        min_bytes: int = 1,  # skip files smaller than this
    ) -> Dict[str, Any]:
        """
        Upload every file in *dir_path* whose extension appears in *extensions* to OpenAI
        and index it into the given vector store, skipping empty files.
        
        Returns a dictionary with upload statistics.
        """
        exts = [ext.lower().lstrip(".") for ext in extensions]
        patterns = (os.path.join(dir_path, f"*.{ext}") for ext in exts)
        file_paths = list(
            itertools.chain.from_iterable(glob.glob(p, recursive=False) for p in patterns)
        )
        
        if not file_paths:
            self._log(f"No files with extensions {exts} found in {dir_path}", "warning")
            return {"uploaded": 0, "skipped": 0, "errors": 0}
        
        stats = {"uploaded": 0, "skipped": 0, "errors": 0}
        
        # Progress tracking
        if self.cli_mode:
            print(f"📁 Found {len(file_paths)} files to process")
            print("-" * 60)
        else:
            progress_bar = st.progress(0)
            status_text = st.empty()
        
        for i, path in enumerate(file_paths):
            filename = os.path.basename(path)
            
            if self.cli_mode:
                print(f"[{i+1}/{len(file_paths)}] Processing: {filename}")
            else:
                progress = (i + 1) / len(file_paths)
                progress_bar.progress(progress)
                status_text.text(f"Processing {filename}...")
            
            # Skip zero-byte (or very small) files
            size = os.path.getsize(path)
            if size < min_bytes:
                self._log(f"Skipping {filename} (size {size} bytes)", "warning")
                stats["skipped"] += 1
                continue
            
            try:
                if self.cli_mode:
                    print(f"  📤 Uploading file to OpenAI...")
                
                with open(path, "rb") as fp:
                    file_resp = self.client.files.create(file=fp, purpose="assistants")
                
                if self.cli_mode:
                    print(f"  🔗 Adding to vector store...")
                
                self.client.vector_stores.files.create(
                    vector_store_id=vector_store_id,
                    file_id=file_resp.id,
                )
                
                self._log(f"Successfully uploaded {filename} (file_id={file_resp.id})", "success")
                stats["uploaded"] += 1
                
                if self.cli_mode:
                    print(f"  ✅ Done!")
                
                time.sleep(0.2)  # gentle rate limit
                
            except BadRequestError as e:
                self._log(f"OpenAI rejected {filename}: {e}", "error")
                stats["errors"] += 1
            except Exception as e:
                self._log(f"Error processing {filename}: {e}", "error")
                stats["errors"] += 1
        
        if not self.cli_mode:
            progress_bar.empty()
            status_text.empty()
        
        return stats
    
    def search_vector_store(self, vector_store_id: str, query: str, search_k: int = 5) -> List[Dict]:
        """
        Queries the OpenAI Vector Store via HTTP and returns up to search_k items.
        """
        if not self.api_key:
            raise ValueError("API key not set")
        
        url = f"https://api.openai.com/v1/vector_stores/{vector_store_id}/search"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v2"
        }
        payload = {"query": query}
        
        try:
            resp = httpx.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json().get("data", [])
            # limit to top search_k
            return data[:search_k]
        except Exception as e:
            st.error(f"Error searching vector store: {e}")
            return []
    
    def answer_question(
        self, 
        vector_store_id: str, 
        question: str, 
        chat_model: str = "gpt-4o-mini",
        temperature: float = 0.2,
        search_k: int = 5
    ) -> str:
        """
        Retrieves relevant passages and asks the chat model to synthesize an answer.
        """
        # 1. Retrieve top passages
        items = self.search_vector_store(vector_store_id, question, search_k)
        
        # 2. Build context string
        context_parts = []
        for item in items:
            filename = item.get("filename", "unknown")
            for passage in item.get("content", []):
                context_parts.append(f"Source: {filename}\n{passage.get('text', '')}")
        context = "\n---\n".join(context_parts)
        
        if not context:
            return "No relevant information found in the knowledge base."
        
        # 3. Create chat messages
        system_msg = {
            "role": "system",
            "content": (
                "You are an expert in Maya archaeology and remote sensing. "
                "Use the provided context to answer precisely, citing sources when relevant. "
                "If the context doesn't contain enough information to answer the question, "
                "say so clearly."
            )
        }
        user_msg = {
            "role": "user",
            "content": (
                f"Context passages:\n{context}\n\n"
                f"Answer the following question: {question}"
            )
        }
        
        # 4. Call chat completion
        try:
            response = self.client.chat.completions.create(
                model=chat_model,
                messages=[system_msg, user_msg],
                temperature=temperature,
                max_tokens=800
            )
            return response.choices[0].message.content
        except Exception as e:
            st.error(f"Error generating answer: {e}")
            return f"Error generating answer: {e}"
    
    def delete_vector_store_files(self, vector_store_id: str) -> int:
        """
        Delete all files associated with a vector store.
        
        Returns the number of files deleted.
        """
        deleted_count = 0
        
        try:
            # List all files in the vector store
            files = self.client.vector_stores.files.list(vector_store_id=vector_store_id)
            
            for file in files.data:
                try:
                    # First, remove the file from the vector store
                    self.client.vector_stores.files.delete(
                        vector_store_id=vector_store_id,
                        file_id=file.id
                    )
                    
                    # Then delete the actual file
                    self.client.files.delete(file.id)
                    self._log(f"✓ Deleted file {file.id}", "success")
                    deleted_count += 1
                    time.sleep(0.1)  # Rate limiting
                    
                except Exception as e:
                    self._log(f"❌ Error deleting file {file.id}: {e}", "error")
                    
        except Exception as e:
            self._log(f"❌ Error listing files for vector store {vector_store_id}: {e}", "error")
        
        return deleted_count
    
    def delete_vector_store(self, vector_store_id: str) -> bool:
        """
        Delete a vector store.
        
        Returns True if successfully deleted, False otherwise.
        """
        try:
            self.client.vector_stores.delete(vector_store_id)
            self._log(f"✓ Deleted vector store {vector_store_id}", "success")
            return True
        except Exception as e:
            self._log(f"❌ Error deleting vector store {vector_store_id}: {e}", "error")
            return False
    
    def cleanup_vector_store(self, vector_store_id: str) -> None:
        """
        Complete cleanup: delete all files and the vector store.
        """
        self._log(f"🧹 Starting cleanup for vector store {vector_store_id}", "info")
        
        # Step 1: Delete all files
        self._log("📄 Deleting files...", "info")
        files_deleted = self.delete_vector_store_files(vector_store_id)
        self._log(f"Deleted {files_deleted} files", "success")
        
        # Step 2: Delete the vector store
        self._log("🗑️ Deleting vector store...", "info")
        if self.delete_vector_store(vector_store_id):
            self._log("✅ Cleanup complete!", "success")
        else:
            self._log("⚠️ Cleanup completed with errors", "warning")
    
    def cleanup_all_vector_stores_by_pattern(self, name_pattern: str = "OpenAI_challenge_") -> None:
        """
        Delete all vector stores whose names start with the given pattern.
        Useful for cleaning up multiple test runs.
        """
        stores = self.client.vector_stores.list()
        matching_stores = [s for s in stores.data if s.name.startswith(name_pattern)]
        
        if not matching_stores:
            self._log(f"No vector stores found matching pattern '{name_pattern}'", "info")
            return
        
        self._log(f"Found {len(matching_stores)} vector stores matching '{name_pattern}'", "info")
        for store in matching_stores:
            self._log(f"\nProcessing: {store.name} (id={store.id})", "info")
            self.cleanup_vector_store(store.id)
    
    def list_all_vector_stores(self) -> List[Dict]:
        """
        List all vector stores with their details.
        """
        try:
            stores = self.client.vector_stores.list()
            return [
                {
                    "id": store.id,
                    "name": store.name,
                    "created_at": store.created_at,
                    "file_counts": store.file_counts if hasattr(store, 'file_counts') else None
                }
                for store in stores.data
            ]
        except Exception as e:
            st.error(f"Error listing vector stores: {e}")
            return []
    
    def list_all_files(self, purpose: Optional[str] = None) -> List[Dict]:
        """
        List all files in OpenAI storage.
        """
        all_files = []
        
        try:
            # OpenAI's list method might paginate, so we need to handle that
            has_more = True
            after = None
            
            while has_more:
                if after:
                    files = self.client.files.list(purpose=purpose, after=after)
                else:
                    files = self.client.files.list(purpose=purpose) if purpose else self.client.files.list()
                
                all_files.extend([
                    {
                        "id": f.id,
                        "filename": f.filename,
                        "purpose": f.purpose,
                        "created_at": f.created_at,
                        "bytes": getattr(f, 'bytes', None)
                    }
                    for f in files.data
                ])
                
                # Check if there are more files
                has_more = files.has_more if hasattr(files, 'has_more') else False
                if has_more and files.data:
                    after = files.data[-1].id
            
            return all_files
            
        except Exception as e:
            st.error(f"❌ Error listing files: {e}")
            return []
    
    def delete_all_files(self, purpose: Optional[str] = None, dry_run: bool = True) -> Dict:
        """
        Delete all files in OpenAI storage.
        
        Returns statistics about the deletion process.
        """
        files = self.list_all_files(purpose=purpose)
        
        if not files:
            self._log("No files found to delete.", "info")
            return {"total": 0, "deleted": 0, "failed": 0}
        
        stats = {
            "total": len(files),
            "deleted": 0,
            "failed": 0,
            "total_bytes": sum(f['bytes'] for f in files if f['bytes'])
        }
        
        if dry_run:
            self._log(f"🔍 DRY RUN - Found {stats['total']} files", "info")
            self._log(f"Total size: {stats['total_bytes'] / (1024*1024):.2f} MB", "info")
            
            self._log("Files that would be deleted:")
            for f in files[:10]:  # Show first 10 files
                created_date = datetime.fromtimestamp(f['created_at']).strftime('%Y-%m-%d %H:%M:%S')
                self._log(f"  - {f['filename']} (ID: {f['id']}, Purpose: {f['purpose']}, Created: {created_date})", "info")
            if len(files) > 10:
                self._log(f"  ... and {len(files) - 10} more files", "info")
            self._log("⚠️ Run with dry_run=False to actually delete these files", "warning")
            return stats
        
        # Actual deletion
        self._log("🗑️ Deleting files...", "info")
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, file in enumerate(files):
            progress = (i + 1) / len(files)
            progress_bar.progress(progress)
            status_text.text(f"Deleting {file['filename']}...")
            
            try:
                self.client.files.delete(file['id'])
                stats["deleted"] += 1
                self._log(f"✓ Deleted {file['filename']} ({i+1}/{stats['total']})", "success")
                time.sleep(0.1)  # Rate limiting
                
            except Exception as e:
                stats["failed"] += 1
                self._log(f"❌ Failed to delete {file['filename']}: {e}", "error")
        
        progress_bar.empty()
        status_text.empty()
        
        self._log("✅ Deletion complete!", "success")
        self._log(f"   Deleted: {stats['deleted']}", "info")
        self._log(f"   Failed: {stats['failed']}", "info")
        
        return stats 