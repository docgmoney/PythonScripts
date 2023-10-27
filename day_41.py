#Website Rate cataloger...why.... idk...
print("Website Rating Cataloger!")

#Creates the empty dictionary
web_rating = {}

#Get user input data
name = input("What is the webistes name?: \n")
url = input("What is the URL of the desired webpage?: \n")
description = input("What would you like to describe this site as?: \n")
rating = int(input("On a scale of 1 to 5 stars; how many stars would you rate this site?: \n"))

#print the catalog page relevant to the new entry...
print(f"""🎭WebRater presents {name} at the url of {url} has been described as {description}.
With an Astonishing {rating} star rating!🎭""")
