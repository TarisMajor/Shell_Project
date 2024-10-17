# Command_Packages/grep.py
import re

def grep(**kwargs):
    # Grep doesn't handle flags but handles params
    flags = kwargs.get("flags")
    params = kwargs.get("params")
    
    #Grep gets the first parameter as a pattern which is a string
    pattern = params[0] 
    
    #grep gets the next parameter as the file to read from
    file = params[1]
    