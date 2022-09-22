#Main game structure
def new_game()
    questions = prep_questions(
        QUESTION, number_questions = NUMBER_QUESTION_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternative) in enumerate(questions, start=1):
        print(f"question {num}:")
        num_correct += ask_question(question, alternatives)
    print(f"You got {num_correct} out of {num} questions correct!!")