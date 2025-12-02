#!/usr/bin/env python3
"""
Compress.py
Sashank Kharal
Assignment 2
"""

import os
import tarfile

def compress(target_dir, output_file): # compress all files in a folder into a tar.gz archive

    tar = tarfile.open(output_file, "w:gz") # open the tar.gx file manually

    for item in os.listdir(target_dir): #loop through all itemin target directory
        full_path = os.path.join(target_dir, item) #get the full path of the item
        
        if os.path.isfile(full_path):  # it only include files
            tar.add(full_path, arcname=item) # add file to archive with just the filename

    tar.close() #close the tar archive

    print("Compression completed!")
