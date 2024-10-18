def head(**kwargs):
    """       
    NAME
       head - output the first part of files

    SYNOPSIS
       head [OPTION]... [FILE]...

    DESCRIPTION
       Print  the  first  10 lines of each FILE to standard output.  With more than one FILE, precede each with a
       header giving the file name.

       With no FILE, or when FILE is -, read standard input.

       Mandatory arguments to long options are mandatory for short options too.

        -n, --lines=[-]NUM
            print the first NUM lines instead of the first 10; with the leading '-', print all but the last NUM
            lines of each file
    """
    
    flags = kwargs.get("flags")
    params = kwargs.get("params")
    h = ''
    for param in params:
        with open(param, 'r') as file:
            for i in range(10):
                line = file.readline().strip()
                h = h + line + '\n'
    
    return(h)