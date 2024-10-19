# Command_Packages/head.py
from .sqliteCRUD import SqliteCRUD
from .dbCommands import DbCommands
from shell import connSqLite
import sqlite3
import os

db_path = './P01/ApiStarter/data/filesystem.db'   

def head(**kwargs):
    """       
    NAME
       head - output the first part of files

    SYNOPSIS
       head [OPTION]... [FILE]...

    DESCRIPTION
       Print  the  first  10 lines of each FILE to standard output.  With more than one FILE, precede each with a
       header giving the file name.

       With no FILE, or when FILE is -, read standard input.

       Mandatory arguments to long options are mandatory for short options too.

        -n, --lines=[-]NUM
            print the first NUM lines instead of the first 10; with the leading '-', print all but the last NUM
            lines of each file
    """
    
    flags = kwargs.get("flags")
    params = kwargs.get("params")
    h = ''
    
    for param in params:
        if "./P01" in param:
            with open(param, 'r') as file:
                for i in range(10):
                    line = file.readline().strip()
                    h = h + line + '\n'
                file.close()
        else:
            # Connect to the database and look for the file
            if DbCommands.file_exists(db_path, param):
                print(f"The file '{param}' exists in the database.")
                file_ids = DbCommands.get_file_and_dir_id(db_path, param)
                file_id = file_ids[0]
                dir_id = file_ids[1]
                content = DbCommands.get_Content(db_path, file_id, dir_id)
                lines = content.splitlines()
                for line in lines[:10]:
                    h = h + line + '\n'
                # Close the connection
            else:
                return(f"The file '{param}' does not exist in the database.")

               
    return(h)