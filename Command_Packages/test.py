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
    
    cwd = '9'
    
    if cwd.isdigit():
        cwd = int(cwd)
    
           
    print(cwd)
