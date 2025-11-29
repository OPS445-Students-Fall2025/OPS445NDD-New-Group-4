#!/usr/bin/env python3

'''
Author: Wayson Cao
Student number: 130300239
'''
import subprocess
import tarfile
import zipfile

def restore(backup_file, restore_path):
    #Purpose: To restore a compressed backup file
    #Brainstorming: use subprocess.open like a1 to run tar cmd or use tarfile  or zipfile
     