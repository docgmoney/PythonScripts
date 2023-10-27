import time
import os
import pandas

count = 0
# 10 second loop
while True:
    path = r"C:\Users\dakot\Desktop\School\Complete Python Course with 10 Real-World Projects\Me\learning\fruits.txt"
    if os.path.exists(path):
        with open(path) as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)
    

    if count == 10:
        print("Program duration reached... Thank you for using.... Come again...")
        break
    else:
        count +=1
