#!/usr/bin/env python3

'''
Author: Wayson Cao
Student number: 130300239
'''

import tarfile

def restore(backup_file, restore_path):
    #Purpose: To restore a compressed backup file
    #Brainstorming: use subprocess.open like a1 to run tar cmd or use tarfile  or zipfile

    tar = tarfile.open(backup_file, 'r') # Reads backup file
    tar.extractall(path=restore_path) # extract tar (backup file), path= where the backup file gets extracted to


     