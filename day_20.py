print("List Generator")
start = int(input("What is the starting number?: \n"))
end = int(input("What is the ending number?: \n"))
increment = int(input("What should the increment be?: \n"))
gen_list = list(range(start, end + 1, increment))
print("Generated list with your parameters: \n", gen_list)
