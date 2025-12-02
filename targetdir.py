#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program:targetdir.py
Author Agnestra Mahat
Description: imports the os module 
            contains the function that checks for files and folders in target_dir
            loops through each file and folder and creates list 
         



'''
import os

def files_list(target_dir):
    #This finction gets the list of files in our target directory and returns a list includes subdirectores but does not go through them.
    
    # This is the empty list to store all the files
    files = []
    
    # Gets all items (files and folders)in the target_dir
    items = os.listdir(target_dir)
    
    # Loop through each item in the target_dir
    for item in items:
        
        #adds the target directory name and  and the filename to create a full pathname [fullpathname is required to check if it is a file or a sub_dir]
        full_path = os.path.join(target_dir, item)

        #append everything to the list of files 
        files.append(full_path)
    
    # Return the list of file paths
    return files



