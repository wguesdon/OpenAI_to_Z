#!/usr/bin/env python3
"""
Script to clean up OpenAI Vector Stores and files.

Usage:
    python cleanup_vector_stores.py --list-stores
    python cleanup_vector_stores.py --cleanup-store "store_name"
    python cleanup_vector_stores.py --cleanup-all-pattern "OpenAI_challenge_"
    python cleanup_vector_stores.py --delete-all-files --dry-run
"""

import os
import argparse
import sys
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

def main():
    parser = argparse.ArgumentParser(
        description="Clean up OpenAI Vector Stores and files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cleanup_vector_stores.py --list-stores
  python cleanup_vector_stores.py --cleanup-store "my_knowledge_base"
  python cleanup_vector_stores.py --cleanup-all-pattern "OpenAI_challenge_"
  python cleanup_vector_stores.py --delete-all-files --dry-run
  python cleanup_vector_stores.py --delete-all-files --purpose assistants
        """
    )
    
    # Mutually exclusive group for main actions
    action_group = parser.add_mutually_exclusive_group(required=True)
    
    action_group.add_argument(
        "--list-stores",
        action="store_true",
        help="List all vector stores"
    )
    
    action_group.add_argument(
        "--cleanup-store",
        type=str,
        help="Clean up a specific vector store by name"
    )
    
    action_group.add_argument(
        "--cleanup-all-pattern",
        type=str,
        help="Clean up all vector stores matching a name pattern"
    )
    
    action_group.add_argument(
        "--delete-all-files",
        action="store_true",
        help="Delete all files in OpenAI storage"
    )
    
    # Optional arguments
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be deleted without actually deleting (for file deletion)"
    )
    
    parser.add_argument(
        "--purpose",
        type=str,
        help="Only delete files with specific purpose (e.g., 'assistants', 'fine-tune')"
    )
    
    args = parser.parse_args()
    
    # Load environment
    api_key = load_environment()
    
    # Initialize vector store manager
    vs_manager = VectorStoreManager(api_key, cli_mode=True)
    
    try:
        if args.list_stores:
            print("📋 Listing all vector stores...")
            stores = vs_manager.list_all_vector_stores()
            
            if not stores:
                print("No vector stores found.")
                return
            
            print(f"\nFound {len(stores)} vector store(s):")
            print("-" * 80)
            for store in stores:
                print(f"ID: {store['id']}")
                print(f"Name: {store['name']}")
                print(f"Created: {store['created_at']}")
                if store['file_counts']:
                    print(f"Files: {store['file_counts']}")
                print("-" * 80)
        
        elif args.cleanup_store:
            print(f"🧹 Cleaning up vector store: {args.cleanup_store}")
            
            # Find the vector store by name
            stores = vs_manager.list_all_vector_stores()
            target_store = None
            
            for store in stores:
                if store['name'] == args.cleanup_store:
                    target_store = store
                    break
            
            if not target_store:
                print(f"❌ Vector store '{args.cleanup_store}' not found")
                print("Available stores:")
                for store in stores:
                    print(f"  - {store['name']}")
                sys.exit(1)
            
            # Confirm deletion
            response = input(f"Are you sure you want to delete vector store '{args.cleanup_store}' and all its files? (yes/no): ")
            if response.lower() != 'yes':
                print("Operation cancelled.")
                return
            
            vs_manager.cleanup_vector_store(target_store['id'])
        
        elif args.cleanup_all_pattern:
            print(f"🧹 Cleaning up all vector stores matching pattern: {args.cleanup_all_pattern}")
            
            # Confirm deletion
            response = input(f"Are you sure you want to delete all vector stores matching '{args.cleanup_all_pattern}'? (yes/no): ")
            if response.lower() != 'yes':
                print("Operation cancelled.")
                return
            
            vs_manager.cleanup_all_vector_stores_by_pattern(args.cleanup_all_pattern)
        
        elif args.delete_all_files:
            print("🗑️ Deleting all files in OpenAI storage...")
            
            if args.purpose:
                print(f"Purpose filter: {args.purpose}")
            
            if args.dry_run:
                print("🔍 DRY RUN MODE - No files will be actually deleted")
                stats = vs_manager.delete_all_files(purpose=args.purpose, dry_run=True)
            else:
                # Confirm deletion
                response = input("Are you sure you want to delete ALL files in OpenAI storage? (yes/no): ")
                if response.lower() != 'yes':
                    print("Operation cancelled.")
                    return
                
                stats = vs_manager.delete_all_files(purpose=args.purpose, dry_run=False)
            
            print(f"\n📊 Deletion Statistics:")
            print(f"  Total files: {stats['total']}")
            print(f"  Deleted: {stats['deleted']}")
            print(f"  Failed: {stats['failed']}")
            if stats['total_bytes']:
                print(f"  Total size: {stats['total_bytes'] / (1024*1024):.2f} MB")
    
    except KeyboardInterrupt:
        print("\n⚠️ Operation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 