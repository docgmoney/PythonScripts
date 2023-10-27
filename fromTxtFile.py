#Creating Variables
myfile = open("fruits.txt")
content = myfile.read()
count = 0

while count <3:
    print(content)
    count += 1
    if count == 3:
        myfile.close()