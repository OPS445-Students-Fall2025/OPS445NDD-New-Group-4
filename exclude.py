#!/usr/bin/env python3

'''
Author: Wayson Cao
Student number: 130300239
'''

# Checks a list of exclude instead from target directory, if sub directory have nothing return the list
def exclude(file_list, sub_dir):
    if sub_dir == None:
        return file_list

