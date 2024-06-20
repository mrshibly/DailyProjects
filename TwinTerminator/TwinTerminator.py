import os
import hashlib
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

logging.basicConfig(filename='duplicate_files.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

def hash_file(file_path):
    """Generate SHA-256 hash for a file."""
    hash_algo = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
    except Exception as e:
        logging.error(f"Error hashing file {file_path}: {e}")
        return None

def find_duplicates(root_folder, dry_run=False):
    """Find duplicate files in the given root folder."""
    hashes = {}
    duplicates = []

    # Traverse the file system and compute hashes
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)
            if file_hash:
                if file_hash in hashes:
                    duplicates.append(file_path)
                else:
                    hashes[file_hash] = file_path

    # Ask for confirmation before deleting each duplicate
    for duplicate in duplicates:
        print(f"Duplicate found: {duplicate}")
        if not dry_run:
            confirm = input("Do you want to delete this duplicate? (y/n): ")
            if confirm.lower() == 'y':
                try:
                    os.remove(duplicate)
                    logging.info(f"Deleted duplicate file: {duplicate}")
                    print(f"Deleted duplicate file: {duplicate}")
                except Exception as e:
                    logging.error(f"Error deleting file {duplicate}: {e}")
                    print(f"Error deleting file {duplicate}: {e}")
            else:
                print(f"Skipped deleting: {duplicate}")
                logging.info(f"Skipped deleting: {duplicate}")
        else:
            print(f"(Dry run) Skipped deleting: {duplicate}")

    # Summary report
    print("\nSummary Report:")
    print(f"Total duplicates found: {len(duplicates)}")
    if not dry_run:
        print(f"Total duplicates deleted: {sum(1 for d in duplicates if os.path.exists(d))}")

def find_duplicates_multithreaded(root_folder, dry_run=False, num_threads=4):
    """Find duplicate files using multithreading."""
    hashes = {}
    duplicates = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_file = {executor.submit(hash_file, os.path.join(dirpath, filename)): os.path.join(dirpath, filename)
                          for dirpath, _, filenames in os.walk(root_folder) for filename in filenames}

        for future in tqdm(as_completed(future_to_file), total=len(future_to_file)):
            file_path = future_to_file[future]
            try:
                file_hash = future.result()
                if file_hash:
                    if file_hash in hashes:
                        duplicates.append(file_path)
                    else:
                        hashes[file_hash] = file_path
            except Exception as e:
                logging.error(f"Error processing file {file_path}: {e}")

    # Ask for confirmation before deleting each duplicate
    for duplicate in duplicates:
        print(f"Duplicate found: {duplicate}")
        if not dry_run:
            confirm = input("Do you want to delete this duplicate? (y/n): ")
            if confirm.lower() == 'y':
                try:
                    os.remove(duplicate)
                    logging.info(f"Deleted duplicate file: {duplicate}")
                    print(f"Deleted duplicate file: {duplicate}")
                except Exception as e:
                    logging.error(f"Error deleting file {duplicate}: {e}")
                    print(f"Error deleting file {duplicate}: {e}")
            else:
                print(f"Skipped deleting: {duplicate}")
                logging.info(f"Skipped deleting: {duplicate}")
        else:
            print(f"(Dry run) Skipped deleting: {duplicate}")

    # Summary report
    print("\nSummary Report:")
    print(f"Total duplicates found: {len(duplicates)}")
    if not dry_run:
        print(f"Total duplicates deleted: {sum(1 for d in duplicates if os.path.exists(d))}")

if __name__ == "__main__":
    root_folder = input("Enter the path of the drive or folder to scan for duplicates: ")
    if os.path.isdir(root_folder):
        dry_run = input("Do you want to perform a dry run? (y/n): ").lower() == 'y'
        num_threads = int(input("Enter the number of threads to use (default 4): ") or 4)
        find_duplicates_multithreaded(root_folder, dry_run=dry_run, num_threads=num_threads)
    else:
        print("The provided path is not a valid directory.")
