# Command_Packages/grep.py
import re
import rich

def grep(**kwargs):
    
    """
    SYNOPSIS
       grep [OPTION...] PATTERNS [FILE...]
       grep [OPTION...] -e PATTERNS ... [FILE...]
       grep [OPTION...] -f PATTERN_FILE ... [FILE...]

    DESCRIPTION
       grep  searches  for  PATTERNS in each FILE.  PATTERNS is one or more patterns separated by newline characters,
       and grep prints each line that matches a pattern.  Typically PATTERNS should be quoted when grep is used in  a
       shell command.

       A  FILE  of  “-”  stands  for  standard  input.   If  no FILE is given, recursive searches examine the working
       directory, and nonrecursive searches read standard input.

       In addition, the variant programs egrep, fgrep and rgrep are  the  same  as  grep -E,  grep -F,  and  grep -r,
       respectively.  These variants are deprecated, but are provided for backward compatibility.
    """
    
    # Grep doesn't handle flags but handles params
    flags = kwargs.get("flags")
    params = kwargs.get("params")
    
    #Grep gets the first parameter as a pattern which is a string
    pattern = params[0] 
    
    #grep gets the next parameter as the file to read from
    file = params[1]
    