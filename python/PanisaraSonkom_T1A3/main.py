#import random package to enable randomise character function
#import cowsay to add graphic
# #import character list from character file
# import random
import cowsay
from newcharacter import char_questions, answer_options


    
#Main game set up

#Display all questions and answer options to user one by one
#Allow user to input answer and ensure that they can input lowercase or uppercase
#show user result after completeing the task
def new_game():
    user_guesses = []
    correct_guesses = 0
    question_number = 1

    for key in char_questions:
        print("--------------------")
        cowsay.dragon(key)
        for i in answer_options[question_number-1]:
            print(i)
        user_guess = input("Choose carefully! Enter(A, B, C, or D): ")
        user_guess = user_guess.upper()
        user_guesses.append(user_guess)

        correct_guesses += check_answer(char_questions.get(key), user_guess)
        question_number += 1
    display_score(correct_guesses,user_guesses)
#display_score(correct_guesses, user_guess)
#check user input with dictionary value
def check_answer(answer,user_guess):

    if answer == user_guess:
        print("Correct!! The Throne is nearly yours")
        return 1
    else:
        print("Wrong! Careful, you are getting reckless.")
        return 0
#let user see their result
def display_score(correct_guesses, user_guesses):
    print("--------------------")
    cowsay.dragon("YOUR RESULTS")
    print("--------------------")

    print("Answer key: ", end="")
    for i in char_questions:
        print(char_questions.get(i), end = " ")
    print()

    print("Your Guesses: ", end = "")
    for i in user_guesses:
        print(i, end= " ")
    print()

    total_score = int((correct_guesses/len(char_questions))*100)
    cowsay.dragon("You got:" + str(total_score) + "%!! Congratulations!")
#Allow user to play again
def play_again():
    user_command = input("Do you want to try and fight for the Throne again? (yes or no): ")
    user_command = user_command.upper()

    if user_command == "yes":
        return True
    else:
        return False



new_game()

while play_again():
    new_game()

print("See you again!!")