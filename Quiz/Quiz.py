
#Welcoming into game along with insertting usename
print("Welcome to Movie Mayham!")
username = input("Please enter a username: ")

print(f"Hi {username}! let's get started")

#We will now import the questions from the json file will also 
#putting in to keep score

import json

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

#going to run quiz in this function

def run_quiz(questions):
    score = 0
    for item in questions:
        print(item['question'])
        for idx, option in enumerate(item['options'], start=1):
            print(f"{idx}. {option}")

        answer = input("Your answer: ")
