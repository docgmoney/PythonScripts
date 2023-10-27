print("Welcome to the ESGC")
name = input("What is your name?\n")
year = int(input("What year were you born in?\n"))

print("Checking now.... Please Wait... Bring out your dead!")
print("Checking now.... Please Wait... Bring out your dead!")
print("Checking now.... Please Wait... Bring out your dead!")

if 1925 <= year <= 1946:
  print(name, ", you're a Traditionalist!")
elif 1947 <= year <= 1964:
  print(name, ", you're a Baby Boomer!")
elif 1965 <= year <= 1981:
  print(name, ", you're a part of Gen X!")
elif 1982 <= year <= 1995:
  print(name, ", you're a Millennial... Sorry Dude!")
elif 1996 <= year <= 2015:
  print(name, ", you're a part of Gen Z!")
else:
  print("Tis Just A Flesh Wound!.")
