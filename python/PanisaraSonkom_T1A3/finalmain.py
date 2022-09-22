#import random package to allow question order to be randomise
import random
from finalcharacter import char_question
#Main game structure and functionality
def new_game()
    questions = prep_char_questions(
        char_question, number_questions = NUMBER_QUESTION_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternative) in enumerate(questions, start=1):
        print(f"question {num}:")
        num_correct += ask_question(question, alternatives)
    print(f"You got {num_correct} out of {num} questions correct!!")

#Randomise questions order to add difficulty for player who is playing multiple time
#Allow user to select however many questions they want; IMPORTANT: max 15 questions
def prep_char_questions(questions, number_questions)
    number_questions = min(number_questions, len(questions))
    return random.sample(list(questions.items()), k=number_questions)

#Ensure that the specific answer of the randomise question list is selected
#Display all choices of the questions
#Allow user to input their answer
# check user's answer
#add num_correct count
def ask_char_questions(question, alternatives):
    correct_ans = alternative[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_ans:
        print("Correct!! You have a good chance on the Throne")
        return 1
    else:
        print(Tough luck! the answer was {correct_ans})
        return 0

