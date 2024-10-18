# Command_Packages/head.py
from .sqliteCRUD import SqliteCRUD
from shell import connSqLite
import sqlite3
import os


dataPath = "../P01/ApiStarter/data/"
db_path = './P01/ApiStarter/data/filesystem.db'
dbName = "filesystem.db"


def file_exists(db_path, name):
    """
    Check if a file exists in the SQLite database.

    Parameters:
        db_path (str): Path to the SQLite database.
        file_name (str): Name of the file to search for.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to check if the file exists
    cursor.execute("SELECT EXISTS(SELECT 1 FROM files WHERE name=?)", (name,))
    
    # Fetch the result
    exists = cursor.fetchone()[0] == 1  # returns True if exists, False otherwise

    # Close the connection
    cursor.close()
    conn.close()

    return exists

# # Example usage
# db_path = 'your_database.db'
# file_name = 'example.txt'

# if file_exists(db_path, file_name):
#     print(f"The file '{file_name}' exists in the database.")
# else:
#     print(f"The file '{file_name}' does not exist in the database.")


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
            if file_exists(db_path, param):
                print(f"The file '{param}' exists in the database.")
            else:
                print(f"The file '{param}' does not exist in the database.")

               
    return(h)