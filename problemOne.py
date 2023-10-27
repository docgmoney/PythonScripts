#Creating a sentence maker...
print("Sentence Maker 2000!")

#Function to correcly format...
def sentence_mkr(phrase):
    interrogatives = ("how", "what", "why", "Can", "please")
    capitalized = phrase.title()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
#creates empty list
results = []

#Looping
while True:
    user_input = input("Say something: \n")
    if user_input == "/end":
         break
    else:
        results.append(sentence_mkr(user_input))


print(" ".join(results))

