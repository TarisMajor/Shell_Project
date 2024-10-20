from shell import cwd
from shell import get_CWD
from .dbCommands import DbCommands
import rich


db_path = './P01/ApiStarter/data/filesystem.db'  

def ls(**kwargs):
    """
    NAME
       ls - list directory contents

    SYNOPSIS
       ls [OPTION]... [FILE]...

    DESCRIPTION
       List  information  about the FILEs (the current directory by default).  Sort entries alphabetically if none of
       -cftuvSUX nor --sort is specified.

       Mandatory arguments to long options are mandatory for short options too.

        -a, --all
              do not ignore entries starting with .
              
        -h, --human-readable
              with -l and -s, print sizes like 1K 234M 2G etc.
              
        -l     use a long listing format
    """
    
    flags = kwargs.get("flags")
    params = kwargs.get("params")
        
    cwd = get_CWD()
    
    if "/" in cwd:
        path = cwd.split("/")
        path = path[1:]
    
    file = []
    for location in path:
        if "." in location:
            location.append(dirs)
        dirs = path[:1]
    file = location[0]
    
    
    if not flags:
        if not params:
            for dir in dirs:
                print(dir)
                if DbCommands.dir_exists(db_path, dir):
                    dir_id = DbCommands.get_dir_id(db_path, dir)
                    listing = DbCommands.get_listing(db_path, dir_id)
                    return listing
                else:
                    return("Directory does not exist.")
        else:
            pass
    else:
        pass