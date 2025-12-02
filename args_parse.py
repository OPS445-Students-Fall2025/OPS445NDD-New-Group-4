#!/usr/bin/env python3
"""
Compress.py
Sashank Kharal
Assignment 2
id=137379236
compress subdirectories with exclude
"""

import os 
import tarfile

def compress(target_dir, output_file, subdirs_to_compress=None):
    """
    Compress all subdirectories in target_dir into a tar.gz archive.
    """

#open the tar.gz file for writing manually
    tar = tarfile.open(output_file, "w:gz")

# If no filtered list is provided it get all subdirectories in target_dir
    if subdirs_to_compress is None:
        subdirs_to_compress = [d for d in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, d))]

# it print the list of subdirectories that will be compressed
    print("Subdirectories being compressed:", subdirs_to_compress)

# loop through each subdirectory and add it to the tar archive
    for subdir in subdirs_to_compress:
    # get the full path of the subdirectory
        full_path = os.path.join(target_dir, subdir)
    # add the subdirectory to the archive arcname=subdir and keeps only the folder name in the archive
        tar.add(full_path, arcname=subdir)

# close the tar archive to save changes
    tar.close()
# print confirmation that compression is done
    print("Compression completed!")
