# Command_Packages/history.py

def history():
    def __str__(self):
    # Open the file in read mode
     with open('history.txt', 'r') as file:
        
        data = file.read()
        file.close()

        # Print the content of the file
        print(data)
        #return data


if __name__ == "__main__":
     with open('history.txt', 'r') as file:
        
        data = file.read()
        file.close()

    # Print the content of the file
        print(data)