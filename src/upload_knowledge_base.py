#!/usr/bin/env python3
"""
Script to upload knowledge base documents to OpenAI Vector Store.

Usage:
    python src/upload_knowledge_base.py --dir data/Knowledge_base --name "my_knowledge_base"
    python src/upload_knowledge_base.py --dir data/Deep_Research_reports --name "research_reports"
    python src/upload_knowledge_base.py --upload-all-data --name "complete_knowledge_base"
    python src/upload_knowledge_base.py --dir data --name "all_data_recursive"
"""

import os
import argparse
import sys
from pathlib import Path
from dotenv import load_dotenv
from vector_store_manager import VectorStoreManager

def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please set OPENAI_API_KEY in your .env file")
        sys.exit(1)
    
    return api_key

def validate_directory(dir_path: str) -> bool:
    """Validate that the directory exists and contains files"""
    if not os.path.exists(dir_path):
        print(f"❌ Error: Directory '{dir_path}' does not exist")
        return False
    
    if not os.path.isdir(dir_path):
        print(f"❌ Error: '{dir_path}' is not a directory")
        return False
    
    # Check if directory contains any files
    files = list(Path(dir_path).glob("*"))
    if not files:
        print(f"❌ Error: Directory '{dir_path}' is empty")
        return False
    
    return True

def get_all_data_subfolders():
    """Get all subfolders in the data directory"""
    data_dir = Path("data")
    if not data_dir.exists():
        print("❌ Error: 'data' directory does not exist")
        return []
    
    subfolders = [f for f in data_dir.iterdir() if f.is_dir()]
    return subfolders

def list_files_in_directory(dir_path: str, extensions: list, recursive: bool = True) -> list:
    """List all files in directory with specified extensions"""
    import glob
    import itertools
    
    exts = [ext.lower().lstrip(".") for ext in extensions]
    file_paths = []
    
    if recursive:
        # Use os.walk for recursive search
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if any(file.lower().endswith(f".{ext}") for ext in exts):
                    file_paths.append(os.path.join(root, file))
    else:
        # Non-recursive search
        patterns = (os.path.join(dir_path, f"*.{ext}") for ext in exts)
        file_paths = list(
            itertools.chain.from_iterable(glob.glob(p, recursive=False) for p in patterns)
        )
    return file_paths

def main():
    parser = argparse.ArgumentParser(
        description="Upload knowledge base documents to OpenAI Vector Store",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python upload_knowledge_base.py --dir data/Knowledge_base --name "amazon_archaeology_kb"
  python upload_knowledge_base.py --dir data/Deep_Research_reports --name "research_reports" --extensions md txt
  python upload_knowledge_base.py --upload-all-data --name "complete_knowledge_base"
  python upload_knowledge_base.py --list-data-folders
        """
    )
    
    # Mutually exclusive group for directory selection
    dir_group = parser.add_mutually_exclusive_group(required=True)
    
    dir_group.add_argument(
        "--dir", 
        help="Directory containing knowledge base files"
    )
    
    dir_group.add_argument(
        "--upload-all-data",
        action="store_true",
        help="Upload all subfolders in the data directory"
    )
    
    dir_group.add_argument(
        "--list-data-folders",
        action="store_true",
        help="List all available data subfolders"
    )
    
    parser.add_argument(
        "--name", 
        required=False,
        help="Name for the vector store (required unless --list-data-folders)"
    )
    
    parser.add_argument(
        "--extensions",
        nargs="+",
        default=["pdf", "md", "markdown", "txt"],
        help="File extensions to include (default: pdf md markdown txt)"
    )
    
    parser.add_argument(
        "--min-bytes",
        type=int,
        default=1,
        help="Minimum file size in bytes to upload (default: 1)"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be uploaded without actually uploading"
    )
    
    parser.add_argument(
        "--recursive",
        action="store_true",
        default=True,
        help="Search for files recursively in subdirectories (default: True)"
    )
    
    parser.add_argument(
        "--no-recursive",
        action="store_false",
        dest="recursive",
        help="Only search files in the specified directory, not subdirectories"
    )
    
    args = parser.parse_args()
    
    # Handle list data folders option
    if args.list_data_folders:
        print("📁 Available data subfolders:")
        subfolders = get_all_data_subfolders()
        if not subfolders:
            print("  No subfolders found in data directory")
        else:
            for folder in subfolders:
                print(f"  - {folder.name}")
        return
    
    # Validate required arguments
    if not args.name:
        print("❌ Error: --name is required")
        sys.exit(1)
    
    # Load environment
    api_key = load_environment()
    
    # Initialize vector store manager
    vs_manager = VectorStoreManager(api_key, cli_mode=True)
    
    if args.upload_all_data:
        # Upload all data subfolders
        subfolders = get_all_data_subfolders()
        if not subfolders:
            print("❌ No subfolders found in data directory")
            sys.exit(1)
        
        print(f"📁 Uploading all data subfolders to vector store: {args.name}")
        print(f"📄 Extensions: {', '.join(args.extensions)}")
        print(f"📏 Min file size: {args.min_bytes} bytes")
        print(f"🔍 Dry run: {args.dry_run}")
        print(f"🔄 Recursive: {args.recursive}")
        print(f"📂 Found {len(subfolders)} subfolders:")
        for folder in subfolders:
            print(f"  - {folder.name}")
        print("-" * 50)
        
        if args.dry_run:
            # List all files that would be uploaded
            total_files = 0
            total_size = 0
            
            for folder in subfolders:
                folder_path = str(folder)
                files = list_files_in_directory(folder_path, args.extensions, args.recursive)
                if files:
                    print(f"\n📂 {folder.name}:")
                    folder_size = 0
                    for path in files:
                        size = os.path.getsize(path)
                        folder_size += size
                        total_size += size
                        rel_path = os.path.relpath(path, folder_path)
                        print(f"  - {rel_path} ({size} bytes)")
                    total_files += len(files)
                    print(f"  📊 {len(files)} files, {folder_size / (1024*1024):.2f} MB")
            
            print(f"\n📊 Total: {total_files} files, {total_size / (1024*1024):.2f} MB")
            print("\n⚠️  This was a dry run. Remove --dry-run to actually upload files.")
            return
        
        try:
            # Get or create vector store
            print("🔧 Getting or creating vector store...")
            vector_store_id = vs_manager.get_or_create_vector_store(args.name)
            
            # Upload files from each subfolder
            total_stats = {"uploaded": 0, "skipped": 0, "errors": 0}
            
            for folder in subfolders:
                folder_path = str(folder)
                print(f"\n📂 Processing folder: {folder.name}")
                
                stats = vs_manager.upload_to_vector_store(
                    dir_path=folder_path,
                    vector_store_id=vector_store_id,
                    extensions=tuple(args.extensions),
                    min_bytes=args.min_bytes,
                    recursive=args.recursive
                )
                
                # Accumulate stats
                total_stats["uploaded"] += stats["uploaded"]
                total_stats["skipped"] += stats["skipped"]
                total_stats["errors"] += stats["errors"]
            
            # Print final results
            print("\n" + "="*50)
            print("📊 Final Upload Results:")
            print(f"  ✅ Successfully uploaded: {total_stats['uploaded']}")
            print(f"  ⚠️  Skipped: {total_stats['skipped']}")
            print(f"  ❌ Errors: {total_stats['errors']}")
            print(f"  🆔 Vector Store ID: {vector_store_id}")
            
            if total_stats['uploaded'] > 0:
                print("\n🎉 All knowledge base folders uploaded successfully!")
            else:
                print("\n⚠️  No files were uploaded. Check the directories and extensions.")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    
    else:
        # Upload single directory
        if not validate_directory(args.dir):
            sys.exit(1)
        
        print(f"📁 Directory: {args.dir}")
        print(f"🏷️  Vector Store Name: {args.name}")
        print(f"📄 Extensions: {', '.join(args.extensions)}")
        print(f"📏 Min file size: {args.min_bytes} bytes")
        print(f"🔍 Dry run: {args.dry_run}")
        print(f"🔄 Recursive: {args.recursive}")
        print("-" * 50)
        
        if args.dry_run:
            # List files that would be uploaded
            file_paths = list_files_in_directory(args.dir, args.extensions, args.recursive)
            
            if not file_paths:
                print("❌ No files found with specified extensions")
                sys.exit(1)
            
            print(f"📋 Found {len(file_paths)} files to upload:")
            total_size = 0
            for path in file_paths:
                size = os.path.getsize(path)
                total_size += size
                rel_path = os.path.relpath(path, args.dir)
                print(f"  - {rel_path} ({size} bytes)")
            
            print(f"\n📊 Total size: {total_size / (1024*1024):.2f} MB")
            print("\n⚠️  This was a dry run. Remove --dry-run to actually upload files.")
            return
        
        try:
            # Get or create vector store
            print("🔧 Getting or creating vector store...")
            vector_store_id = vs_manager.get_or_create_vector_store(args.name)
            
            # Upload files
            print("📤 Uploading files to vector store...")
            stats = vs_manager.upload_to_vector_store(
                dir_path=args.dir,
                vector_store_id=vector_store_id,
                extensions=tuple(args.extensions),
                min_bytes=args.min_bytes,
                recursive=args.recursive
            )
            
            # Print results
            print("\n" + "="*50)
            print("📊 Upload Results:")
            print(f"  ✅ Successfully uploaded: {stats['uploaded']}")
            print(f"  ⚠️  Skipped: {stats['skipped']}")
            print(f"  ❌ Errors: {stats['errors']}")
            print(f"  🆔 Vector Store ID: {vector_store_id}")
            
            if stats['uploaded'] > 0:
                print("\n🎉 Knowledge base uploaded successfully!")
            else:
                print("\n⚠️  No files were uploaded. Check the directory and extensions.")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 