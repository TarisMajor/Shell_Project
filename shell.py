import importlib
import pkgutil
import Command_Packages

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


if __name__ == "__main__":
    # Load the commands dynamically from Command_Packages
    load_commands()

    #print(cmds)
    # Example usage:
    cmd = "history"
    params = []

    # Call the function dynamically from the dictionary
    if cmd in cmds:
        result = cmds[cmd]
        #(params=params)
        print(result)
    else:
        print(f"Command '{cmd}' not found.")
        