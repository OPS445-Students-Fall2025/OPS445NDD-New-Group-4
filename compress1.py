#!/usr/bin/env python3
"""
Compress.py
Sashank Kharal
Assignment 2
"""

import os
import tarfile

def compress(target_dir, output_file, subdirs_to_compress=None):  # added subdirs_to_compress parameter

    tar = tarfile.open(output_file, "w:gz")  # open the tar.gz file manually

    # If no subdirs specified, compress everything in target_dir
    if subdirs_to_compress is None:
        subdirs_to_compress = os.listdir(target_dir)

    for item in subdirs_to_compress:  # loop through specified items
        full_path = os.path.join(target_dir, item)  # get the full path

        # include both files and folders
        if os.path.isfile(full_path) or os.path.isdir(full_path):
            tar.add(full_path, arcname=item)  # add to archive

    tar.close()  # close the tar archive

    print("Compression completed!")
