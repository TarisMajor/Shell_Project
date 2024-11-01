# Command_Packages/history.py

def history(**kwargs):
    # History doesn't handle flags nor params so doing nothing with them
    flags = kwargs.get("flags")
    params = kwargs.get("params")
    
    # Open the file in read mode
    with open('./P01/history.txt', 'r') as file:
        
        data = file.read()
        file.close()
        data = data.split("\n")
        dataList = {}
        
        dataList = {index: item for index, item in enumerate(data[:-1])}        
        h = ''
            
        for key, value in dataList.items():
            # print(f"{key}  {value}")
            h = h + f"{key}  {value}\n"

        # print(data)
        return h


if __name__ == "__main__":
     with open('./P01/history.txt', 'r') as file:
         
        data = file.read()
        file.close()
        data = data.split("\n")
        dataList = {}
        
        # for index, item in enumerate(data):
        #     dataList[index] = data
        dataList = {index: item for index, item in enumerate(data[:-1])}
        #print(dataList)
        h = ''
        for key, value in dataList.items():
            # print(f"{key}  {value}")
            h = h + f"{key}  {value}\n"
        print(h)
        #for key, value in dataList.items():
          #  print(f"{key}  {value}")


    # Print the content of the file
        #print(dataList)