# Command_Packages/exclamation.py

def exclamation(**kwargs):

    flags = kwargs.get("flags")
    params = kwargs.get("params")
    
    if params:
        pass
    else:
        return(f'Do nothing')
    
    return(f"Flags: {flags} and Params: {params}")