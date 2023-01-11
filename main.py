# CREATE A QUIZ ASSIGNMENT

# Title 
print("Quiz on No Country for Old Men (2007)")

# Score
score = 0

# Question 1
answer1 = input("Who directs the movie No Country for Old Men? ")
if answer1.casefold() == "the Coen brothers" or answer1.casefold() == "Joel Coen" or answer1.casefold() == "Ethan Coen":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

# Question 2
