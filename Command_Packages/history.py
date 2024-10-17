# Command_Packages/history.py

def history():
    # Open the file in read mode
    with open('history.txt', 'r') as file:
        
        data = file.read()
        file.close()
        data = data.split("\n")
        dataList = {}
        
        dataList = {index: item for index, item in enumerate(data[:-1])}        
            
        for key, value in dataList.items():
            print(f"{key}  {value}")

        # print(data)
        return dataList


if __name__ == "__main__":
     with open('history.txt', 'r') as file:
         
        data = file.read()
        file.close()
        data = data.split("\n")
        dataList = {}
        
        # for index, item in enumerate(data):
        #     dataList[index] = data
        dataList = {index: item for index, item in enumerate(data[:-1])}
        #print(dataList)
        
            
        for key, value in dataList.items():
            print(f"{key}  {value}")


    # Print the content of the file
        #print(dataList)