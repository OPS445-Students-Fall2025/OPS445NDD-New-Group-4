#!/usr/bin/env python3

'''
Author: Wayson Cao
Student number: 130300239
'''

import tarfile

def restore(backup_file, restore_path):
    try:
        tar = tarfile.open(backup_file, 'r:*') # Reads backup file, :* means it open reading with any compression whether it's gipz, lzma, zip2, etc
        tar.extractall(path=restore_path) # extract tar (backup file), path= where the backup file gets extracted to
        tar.close() # Closes archive
        print(f"Your backup file {backup_file} have been extracted to {restore_path}")
    except(FileNotFoundError, tarfile.ReadError): # Double checks whatever in print below
        print(f"ERROR: Your backup file {backup_file} cannot be found or it's not a valid/supported tarfile") 


     
