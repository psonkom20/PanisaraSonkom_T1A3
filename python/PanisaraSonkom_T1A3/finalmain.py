#import random package to allow question order to be randomise
import random
#Main game structure and functionality
def new_game()
    questions = prep_questions(
        QUESTION, number_questions = NUMBER_QUESTION_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternative) in enumerate(questions, start=1):
        print(f"question {num}:")
        num_correct += ask_question(question, alternatives)
    print(f"You got {num_correct} out of {num} questions correct!!")

#Randomise questions order to add difficulty for player who is playing multiple time
#Allow user to select however many questions they want; IMPORTANT: max 15 questions
def prep_questions(questions, number_questions)
    number_questions = min(number_questions, len(questions))
    return random.sample(list(questions.items()), k=number_questions)
