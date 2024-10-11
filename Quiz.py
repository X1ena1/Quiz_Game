#Welcoming into game along with insertting usename
print("Welcome to Movie Mayham!")
print("Please enter your usernme: ")



#Score and 
# questions are getting implemented here
#importing my questions first from my json file
import json


score = 0
qas = {
    "How many SAW movies where produced": "12",
    "What is the capital of Texas": "Austin"
}

for question_num, (question, answer) in enumerate(qas.items(), start=1):
    user_answer = input(f"{question_num}. {question}? ")
    if user_answer == answer:
        score += 1

print(f"Your score is {score}")
