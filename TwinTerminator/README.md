# TwinTerminator

TwinTerminator is a Python tool designed to find and delete duplicate files in a specified directory. It uses multithreading to efficiently hash files and offers a dry run mode for safety. Users are prompted for confirmation before any file is deleted.

## Features

- Efficiently find duplicate files using multithreading
- Prompt user confirmation before deleting files
- Dry run mode to preview duplicates without deletion
- Detailed logging of operations and errors
- Summary report of duplicates found and actions taken

## Installation

Ensure you have Python 3 installed on your system. You can install the required dependencies using pip:

```bash
pip install tqdm
```

## Usage

1. Download the `TwinTerminator` script file directly from the GitHub repository.

2. Run the script by executing:

```bash
python twin_terminator.py
```

### Command-line Inputs

1. **Root Folder**: The path to the folder or drive where you want to scan for duplicates.
2. **Dry Run**: Option to perform a dry run where no files are deleted, but duplicates are listed.
3. **Number of Threads**: The number of threads to use for multithreading (default is 4).

### Example

```bash
Enter the path of the drive or folder to scan for duplicates: /path/to/your/folder
Do you want to perform a dry run? (y/n): y
Enter the number of threads to use (default 4): 4
```

## Logging

Operations and errors are logged to `duplicate_files.log` in the same directory as the script. This log file includes information on all deletions and any errors encountered during execution.

## Summary Report

At the end of the execution, a summary report is displayed with the total number of duplicates found and the number of duplicates deleted (if not in dry run mode).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
