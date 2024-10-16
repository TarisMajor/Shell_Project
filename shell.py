import importlib
import pkgutil
import Command_Packages
from Command_Packages.getch import Getch
import sys

# Dictionary to store the commands
cmds = {}


# Dynamically load all functions from Command_Packages into the dictionary
def load_commands():
    global cmds

    # Loop through all modules in the Command_Packages package
    for _, module_name, _ in pkgutil.iter_modules(Command_Packages.__path__):
        module = importlib.import_module(f"Command_Packages.{module_name}")

        # Loop through the attributes in each module
        for name in dir(module):
            obj = getattr(module, name)
            # Check if it's a callable function and doesn't start with '__'
            if callable(obj) and not name.startswith("__"):
                cmds[name] = obj


# Get the docstring of a function
def get_docstring(func_name):
    if func_name in cmds:
        return cmds[func_name].__doc__
    else:
        return f"Function '{func_name}' not found."
    
def ShellPrompt(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    
    
def get_flags(command):
    flags = []
    for c in command:
        if c.startswith("-") or c.startswith("--"):
            flags.append(c)
    return flags

def get_params(command):
    params = []
    for c in command:
        if "-" in c or "--" in c:
            continue
        params.append(c)
        
    for i, p in enumerate(params[:-1]):
        if (
            params[i].startswith("'")
            and params[i + 1].endswith("'")
            or params[i].startswith('"')
            and params[i + 1].endswith('"')
        ):
            params[i] = params[i] + " " + params[i + 1]
            
    return params


def parse(shellInput):
    
    redirect = None
    
    if ">" in shellInput:
        shellInput, redirect = shellInput.split(">")
    
    if "|" in shellInput:
        subCmds = shellInput.split("|")
    else:
        subCmds = [shellInput]

    cmdList = []
    
    for i in range(len(subCmds)):
       
        cmd = subCmds[i].strip()
        cmd = cmd.split(" ")
        
        cmdDict = {
            "cmd": cmd[0],
            "flags": get_flags(cmd),
            "params": get_params(cmd[1:]),
        }
        cmdList.append(cmdDict)
        # freak | ls -l -a -h | grep cout hav.txt parms.txt
        
    print(cmdList)
    return cmdList
    
def getCommands(commands):
    input = ""
    
    while True:                                 # loop forever
        
        char = getch()  
        input += char
        
        if char == "\x7f":
            input = input[:-2]
            sys.stdout.write('\b \b')
            
        elif char == "\r":
            print(" ")
            break
            
        elif char == "~":
            print(" ")
            break
        
        sys.stdout.write(char)
        sys.stdout.flush()
    return input


if __name__ == "__main__":
    # Load the commands dynamically from Command_Packages
    load_commands()

    
    getch = Getch()                             # create instance of our getch class
    prompt = "%Testing:"                        # set default prompt
    input = ""
    
    ShellPrompt(prompt)

    command = getCommands(input)
    
    commandList = parse(command)
    
    

    # Call the function dynamically from the dictionary
    #if cmd in cmds:
        #result = cmds[cmd]
        #(params=params)
        #print(result)
    #else:
        #print(f"Command '{cmd}' not found.")
        
    sys.exit(0)
        