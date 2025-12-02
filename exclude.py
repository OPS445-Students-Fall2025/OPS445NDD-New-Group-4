#!/usr/bin/env python3

'''
Author: Wayson Cao
Student number: 130300239
'''

def exclude(subdirectories, subdir_to_exclude): # If there is no subdirectory to exclude, leave it be
    if subdir_to_exclude == None:
        return subdirectories

    subdir_not_excluded = []
    for subdir in subdirectories: # For every subdirectory in subdirectories
        if subdir_to_exclude not in subdir: # only selects directories that are not excluded
            subdir_not_excluded.append(subdir) # Add that subdir to not excluded subdirectory list
    return subdir_not_excluded # Return a list of subdirectories to compress