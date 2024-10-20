
def test():
    cwd = "/1000-Spacial_Data_Structures"

    if "/" in cwd:
        path = cwd.split("/")
        
    print(path)

if __name__ == "__main__":
    cwd = "/1000-Spacial_Data_Structures"

    if "/" in cwd:
        path = cwd.split("/")
    
    path = path[1:]
    
    path = path[0]
    print(path)