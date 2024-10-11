#Welcoming into game along with insertting usename
print("Welcome to Movie Mayham!")
print("Please enter your usernme: ")


#importing my questions first from my json file
import json

def questions(Qui_ques):
    with open(Qui_ques, 'r') as files:
        questions = json.load(Qui_ques)
    return questions

def run_quiz(questions):
    score = 0

for question, answer in questions:
    answer = input(f"{question}? ")
    if answer == answer:
        print("Correct!")
    else:
        print(f"The answer is {answer!r}!,")