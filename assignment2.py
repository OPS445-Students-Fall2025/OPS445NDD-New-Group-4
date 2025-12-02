#!/usr/bin/env python3
'''
OPS445 Assignment2
Author: Agnestra Mahat
Author ID:128939238
Program: assignment2.py

'''

# Import necessary functions
from exclude import exclude
from compress1 import compress
from restore import restore
from args_parse import parse_command_args  
import os

# Main Program
if __name__ == "__main__":
    # Get the user input in the command line
    args = parse_command_args()

    # If the compress option is used in the command line argument 
    if args.action == "compress":
        target_dir = args.target  # sets the target directory to compress

        # checks if the target directory exists using the os module
        if not os.path.isdir(target_dir):
            print(f"Error: Target directory '{target_dir}' does not exist.")
            exit(1)

# Make an empty list to store the names of subfolders
subdirs = []
# Loop through every item inside the target directory
for item in os.listdir(target_dir):
    # creates the full pathname for each item 
    full_path = os.path.join(target_dir, item)
    # checks if this item is a subdirectory
    if os.path.isdir(full_path):
        # If it IS a folder, add its name to our subdirs list
        subdirs.append(item)
        # checks if the some directories were required to be skipped
        if args.exclude:
            # based on the exclude condition provided, filters the sub_dirs
            subdirs = exclude(subdirs, args.exclude)
            print(f"Subdirectories after excluding '{args.exclude}': {subdirs}")

        # checks if the name for outputfile is provided if not prints an error message
        if not args.output:
            print("Error: Output file is needed")
            exit(1)

        # compresses the selected sub_dirs
        compress(target_dir, args.output, subdirs_to_compress=subdirs)
        print(f"Compression is completed! Saved as: {args.output}")

    # If the restore option is used
    elif args.action == "restore":
        target_file = args.target  # backup file to restore
        restore_path = args.output  # path  to restore the files

        # checks if the backup fole exists if not prints an error message
        if not os.path.isfile(target_file):
            print(f"Error: Backup file '{target_file}' does not exist.")
            exit(1)

        # uses the current folder as default incase there is no default path.
        if not restore_path:
            restore_path = "."  # current folder

        # restores the backups.
        restore(target_file, restore_path)
        print(f"Restore is completed! Files are in: {restore_path}")
