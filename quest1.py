# from Question import Question
question_prompt = ["What color are apples?\n (a) Red/Green\n(b) Purple\n(c) orange\n\n"
                   "What colr are bananas?\n (a) Teal\n(b) Magenta\n(c) Yellow\n\n"
                   "What color are strawberries?\n (a) Yellow\n(b) Red\n(c) Blue\n\n"]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)