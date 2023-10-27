#Area of a Triangle Calc
def areaOfTriangle(base, height):
    area = 0.5 * base * height
    return area
#Creating loop to use on repeat
i = "y"
while i == "y":
    base = int(input("What is the base of the Triangle?: \n"))
    height = int(input("What is the height of the Triangle?: \n"))
    area = areaOfTriangle(base, height)
    print("The Area of your triangle is", area, "units squared!")
    i = input("Would you like to do another Triangle?: y/n \n")
 