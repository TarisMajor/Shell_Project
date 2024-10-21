# Command_Packages/grep.py
import re
from rich.console import Console
from rich.text import Text

def replace_pattern(text, pattern, replacement):
    # Define a function to format the replacement text
    def format_replacement(match):
        return Text(replacement, style="bold red")

    # Use regex to substitute the pattern with formatted text
    new_text = re.sub(pattern, format_replacement, text)
    return new_text

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
    console = Console()
    #grep gets the next parameter as the file to read from
    file = params[-1]
    
    if ".txt" in file:
       with open(file, 'r') as open_file:
          for line_number, line in enumerate(open_file, start=1):
                if pattern in line:
                  replace_pattern = pattern
                  line = replace_pattern(line, pattern, replace_pattern)
                  console.print(f"{line.strip()}")
                    
    