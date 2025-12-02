#!/usr/bin/env python3
"""
Sashank Kharal
137379236
args_parse
"""
import argparse

def parse_command_args():
    """parse command line arguments and return them as an object."""
    parser = argparse.ArgumentParser( 
        description="data backup and restore and subdirectories can be excluded as needed"
    )
    #create a parser with a description
    parser.add_argument("action", choices=["compress", "restore"], help="Action to perform: compress or restore")
    #choose what to do compress or restore
    parser.add_argument("target", help="Target directory (for compress) or backup file (for restore)")
    #folder to compress or backup file to restore
    parser.add_argument("-o", "--output", help="Output file for compression or restore path")
     #name or path of the output file
    parser.add_argument("--exclude", help="Subdirectory name to exclude (optional)")
     #subdirectory to skip if needed
    args = parser.parse_args() #read the arguments from the command line  
    return args