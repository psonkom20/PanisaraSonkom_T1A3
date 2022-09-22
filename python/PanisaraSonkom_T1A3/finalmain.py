#import random package to allow question order to be randomise
import random
from finalcharacter import char_question
from string import ascii_uppercase

#Welcome page
#cowsay.dragon

#Main game structure and functionality
NUMBER_QUESTION_PER_QUIZ = 15
def new_game():
    questions = prep_char_questions(
        char_question, number_questions = NUMBER_QUESTION_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"question {num}:")
        num_correct += ask_char_questions(question, alternatives)
    print(f"You completed the quiz!! You got {num_correct} out of {num} questions correct. But you can only sit on the throne if you got all the question. So if you did, Congrats!!! The Throne is yours")

#Randomise questions order to add difficulty for player who is playing multiple time
#Allow user to select however many questions they want; IMPORTANT: max 15 questions
def prep_char_questions(questions, number_questions):
    number_questions = min(number_questions, len(questions))
    return random.sample(list(questions.items()), k=number_questions)

#Ensure that the specific answer of the randomise question list is selected
#Display all choices of the questions
# check user's answer
#add num_correct count
#seperate into two functions for readability
def ask_char_questions(question, alternatives):
    correct_ans = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_char_answer(question, ordered_alternatives)
    if answer == correct_ans:
        print("Correct!! You have a good chance on the Throne")
        return 1
    else:
        print("Tough luck! The answer was {correct_ans}")
        return 0
#Allow user to input their answer
#Label alternative choice
#if user enter choice that is not available allow them to answer again
def get_char_answer(question, alternatives):
    print(f"{question}")
    labeled_choice = dict(zip(ascii_uppercase, alternatives))
    for label, alternative in labeled_choice.items():
        print(f" {label} {alternative}")
    while (ans_label := input("Enter your answer (A, B, C, or D): ")) not in labeled_choice:
        print(f"Not an option; Please choose between A, B, C, or D")
    return labeled_choice[ans_label]
def play_again():
    user_command = input("Do you want to try and fight for the Throne again? (yes or no): ")
    user_command = user_command.upper()

    if user_command == "YES":
        return True
    else:
        return False

    
if __name__ == "__main__":
    new_game()

    while play_again():
        new_game()
    
    print("Thanks for playing!!")