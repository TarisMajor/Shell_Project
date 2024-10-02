#!/usr/bin/env python
import subprocess
import os
import stat


def ls(*flags):
    """This is my manpage entry for the pwd command"""
    #folder = kwargs.get("params", [])
    #result = subprocess.run(["ls", "-lah", folder[0]], stdout=subprocess.PIPE)

    # return result.stdout.decode("utf-8")
    for flag in flags:
        print(f"{flag}")

 
 #use the os library to get the last modified date, permissions, owner and such
 
 #Ls = ls(*testFlags)