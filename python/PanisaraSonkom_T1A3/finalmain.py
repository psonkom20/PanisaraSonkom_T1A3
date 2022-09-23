#import random package to allow question order to be randomise
import random
import cowsay
from finalcharacter import char_question
from string import ascii_uppercase

#Welcome page
#Add instruction of game
#Ask user how many question they want
cowsay.dragon("Welcome! Are you ready to fight for the Throne?\n The game is simple. You'll be given a quote and\n ask which character said it. You have four\n character options but one chance to guess so\n answer carefully!! Goodluck!")
def get_int():
    return int(input("How many questions would you like? There is a maximum of 15 question: "))
while True:     
    try:
        user_number_q_per_game = get_int()
        print(f"This quiz will have {user_number_q_per_game} questions")
        break
    except ZeroDivisionError:
        print('Input cannot be 0 and MUST be between 1-15')
        break
print("------------------------------------------------------------------------------------------------------------------------")
#Main game structure and functionality
def new_game():
    questions = prep_char_questions(
        char_question, user_number_q_per_game)
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print("------------------------------------------------------------------------------------------------------------------------")
        print(f"Question {num}:")
        num_correct += ask_char_questions(question, alternatives)
    total_score_perc = int((num_correct/num)*100)
    print("------------------------------------------------------------------------------------------------------------------------")
    cowsay.dragon(f"You completed the quiz!! You got {num_correct} out of {num}\n questions. A " +str(total_score_perc) + " %!! You can only sit on the\n throne if you got all the question. So if\n you did, Congrats!!! The Throne is yours!!!\n If not try againg!!")
    print("------------------------------------------------------------------------------------------------------------------------")

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
        cowsay.dragon("Correct!! You have a good chance on the Throne")
        return 1
    else:
        cowsay.dragon(f"Tough luck! The answer was {correct_ans!r}")
        return 0
#Allow user to input their answer
#Label alternative choice
#if user enter choice that is not available allow them to answer again
def get_char_answer(question, alternatives):
    print(f"{question}")
    print("------------------------------------------------------------------------------------------------------------------------")
    labeled_choice = dict(zip(ascii_uppercase, alternatives))
    for label, alternative in labeled_choice.items():
        print(f" {label}. {alternative}")
 
    while (ans_label := input("Enter your answer (A, B, C, or D): ")) not in labeled_choice:
        print(f"Not an option. Be sure to capitalise your answer. Please choose between A, B, C, or D")
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
        
    
    cowsay.dragon("Thanks for playing!!")