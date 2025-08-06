# we see one more example to understand 2D list even more
# *** this is a good program try to understand it properly ***
# Python - Quiz Game

questions = ("how many elements are there in the periodic table?:",
             "which animal lays the largest egg?:",
             "what is the most abundant gas in the earht's atmosphere:?",
             "how many bones are there in the human body?:",
             "wich planet in the solar system is the hottest?:")

options = (("A.116","B.117","C.118","D.119"),
           ("A. Ostrich", "B. Elephant", "C. Blue Whale", "D. Emu"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"),
           ("A. 206", "B. 208", "C. 210", "D. 212"),
           ("A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"))

# note questions is a normal tuple and options is a 2d tuple
# answering mechainism

answers = ["C","D","A","A","B"]
guesses = [] # intializing a list
score = 0 # initializing score to 0
question_num = 0

for question in questions:
    print("------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = str(input("enter your choice(A,B,C,D ): "))
    guesses.append(guess)
    if guess == answers[question_num]:
        print("you guessed correctly")
        score += 1
    else:
        print("wrong answer")
        print(f"the correct answer is {answers[question_num]}")

    question_num += 1
print(f"the guesses were {guesses}")
print(f"the total score was {score} out of {len(questions)}")