# Command_Packages/mv.py
from shell import cwd
import sqlite3
import os
#from sqliteCRUD import SqliteCRUD

# def dbConnect():
#     dataPath = "../P01/ApiStarter/data/"
#     dbName = "filesystem.db"
#     if os.path.exists(os.path.join(dataPath, dbName)):
#         fsDB = SqliteCRUD(os.path.join(dataPath, dbName))
#     else:
#         print("Database file not found.")
#         fsDB = None

def mv(**kwargs):
    """
    NAME
       mv - move (rename) files

    SYNOPSIS
       mv [OPTION]... SOURCE... DIRECTORY
       mv [OPTION]... -t DIRECTORY SOURCE...

    DESCRIPTION
       Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.
    """
    
    # MV doesn't handle flags but handles params
    flags = kwargs.get("flags")
    params = kwargs.get("params")
    
    dataPath = "./data/"
    dbName = "filesystem.db"
    if os.path.exists(os.path.join(dataPath, dbName)):
        fsDB = SqliteCRUD(os.path.join(dataPath, dbName))
    else:
        print("Database file not found.")
        fsDB = None