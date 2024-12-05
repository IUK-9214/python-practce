import random
one = "What is Your name?"
two = "Where are you from?"
three = "What is your fathers name?"
four = "What is your mothers name?"
five = "What is your brothers name?"
six = "What is your sisters name?"
seven = "What is your friends name?"
eight = "What is your pet name?"
nine = "What is your favourite animal?"
questions = ([one,two,three,four,five,six,seven,eight,nine])
random.shuffle(questions)
for i in questions:
    answer = input(f"{i} ")
print("All Questions Answered!")
