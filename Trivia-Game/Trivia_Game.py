# list of questions 
# Store answers
# randomly pick 3 questions 
# see if they are correct
# count score 
import random

python_qa = {
    "what is python": "interpreted language",
    "who created it": "guido van rossum",
    "file extension": ".py",
    "case sensitive": "yes",
    "code block style": "indentation",
    "list mutability": "mutable",
    "tuple mutability": "immutable",
    "unique collection": "set",
    "key-value storage": "dictionary",
    "define function": "def keyword",
    "anonymous function": "lambda",
    "empty placeholder": "pass",
    "package manager": "pip",
    "style guide": "pep 8",
    "check identity": "is operator",
    "check equality": "== operator"
}

def trivia_game():
    qa_list=list(python_qa.keys())
    total_qa= 3
    score = 0

    selected_qa =random.sample(qa_list,total_qa)

    for idx,question in enumerate(selected_qa):
        print(f"{idx + 1}.{question}")
        user_answer = input("Your Answer: ").lower().strip()

        correct_ans=python_qa[question]
        if user_answer == correct_ans:
            print("Correct\n")
            score += 1
        else:
            print(f"Wrong, The correct answer is: {correct_ans}")
    
    print(f"Game Over! Your final Score is {score}/{total_qa}")

def u_return():
    return

User_Choice= int(input('''
            1 . Play
            2 . Exit
    '''))

if User_Choice == 1:
    trivia_game()
elif User_Choice == 2:
    u_return()
else:
    print("Choose the Valid Digit")
