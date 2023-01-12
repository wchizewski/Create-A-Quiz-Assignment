# CREATE A QUIZ ASSIGNMENT - NO COUNTRY FOR OLD MEN (2007) QUIZ

# Title 
print("Quiz on No Country for Old Men (2007)")

# Score
score = 0

# Question 1
answer1 = input("Who directs the movie No Country for Old Men? ")
if answer1.casefold() == "the coen brothers" or answer1.casefold() == "joel coen" or answer1.casefold() == "ethan coen":
    print("☑ Correct")
    score = score + 1
else:
    print("☒ Incorrect")

# Question 2
answer2 = input("How much money does LLewelyn Moss stumble across in the desert at the botched drug deal? ")
if answer2.casefold() == "two million dollars" or answer2.casefold() == "$2 million" or answer2.casefold() == "$2000000":
    print("☑ Correct")
    score = score + 1
else:
    print("☒ Incorrect")

# Question 3
answer3 = input("What is the name of the man who was hired to kill Anton Chigurh and retrieve the money but fails? ")
if answer3.casefold() == "carson wells" or answer3.casefold() == "carson" or answer3.casefold() == "wells":
    print("☑ Correct")
    score = score + 1
else:
    print("☒ Incorrect")

# Question 4
answer4 = input("Who is falsely foreshadowed to be waiting for Sheriff Ed Tom Bell at the hotel room crime scene where Llewelyn was murdered? ")
if answer4.casefold() == "anton chigurh" or answer4.casefold() == "anton" or answer4.casefold() == "chigurh":
    print("☑ Correct")
    score = score + 1
else:
    print("☒ Incorrect")


# Quiz Result Output
percent = score / 4 * 100
print("Your score is " + str(score) + " / 4 (" + str(percent) + "%)")
if score <= 2:
    print("You need to watch the movie again!")
else:
    print("Great Work!")