# Command_Packages/pwd.py
from shell import cwd

def pwd(**kwargs):
    """
    NAME
       pwd - print name of current/working directory

    SYNOPSIS
       pwd [OPTION]...

    DESCRIPTION
       Print the full filename of the current working directory.
    """
    
    # PWD doesn't handle flags nor params
    flags = kwargs.get("flags")
    params = kwargs.get("params")
    
    return(cwd)