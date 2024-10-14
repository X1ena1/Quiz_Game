#We will now import the questions from the json
import json

#Welcoming into game along with insertting usename
print("Welcome to Movie Mayham!")
username = input("Please enter a username: ")

print(f"Hi {username}! let's get started")

#defining the questions from our json file

file_path = "Ques.json"

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

#going to run quiz in this function
#score is gonna be the start of how manny questions and after every question correct
#1 is going to be added
def run_quiz(questions):
    score = 0

    for item in questions:
        print(item['question'])
        if 'options' in item:
            for idx, option in enumerate(item['options'], start=1):
                print(f"{idx}. {option}")

            answer = input("Your answer: ")
            
            #checking to see it the answer is correct


questions = load_questions(file_path)
run_quiz(questions)