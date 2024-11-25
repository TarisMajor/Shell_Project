import sys

class Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): 
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
    
def ShellPrompt(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()

if __name__=='__main__':

    getch = Getch()                             # create instance of our getch class
    prompt = "%Testing:"                        # set default prompt
    input = ""
    
    ShellPrompt(prompt)

    while True:                                 # loop forever
        
        char = getch()  
        input += char
        
        if char == "\x7f":
            input = input[:-2]
            sys.stdout.write('\b \b')
            
        elif char == "\r":
            print(" ")
            print(input)
            break
            
        elif char == "~":
            print(" ")
            break
        
        sys.stdout.write(char)
        sys.stdout.flush()
        #echo(input)
        
        