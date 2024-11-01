import base64
import requests

def encodeIt(plainText):
    # Encode the string as bytes, then to Base64
    encoded = base64.b64encode(plainText.encode("utf-8"))
    # Convert back to string for display
    return encoded


def decodeIt(encodedText):
    # Decode Base64 to original bytes
    decoded = base64.b64decode(encodedText)
    # Convert bytes back to string
    return decoded.decode("utf-8")

def test():
    cwd = "!!!!!9"
    
    cwd = list(cwd)
    cmd = cwd.split(" ")

    if "/" in cwd:
        path = cwd.split("/")
        
    print(path)

if __name__ == "__main__":
    
    cwd = "!!!!!9"
    
    cwd = list(cwd)
    
    command = cwd[0]
    params = cwd[1:]
    params = ''.join(params)
    
    sub = []
    sub.append(command)
    sub.append(params)
    subcmd = [sub]
    
    for i in range(len(subcmd)):
        
        try:
           cmd = subcmd[i].strip()
           cmd = cmd.split(" ")
        except:
           cmd = subcmd[i]
           
    print(cwd)
    print(command)
    print(params)
    
    print(subcmd)