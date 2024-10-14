#Importting the questions from the json
import json

#Welcoming into game along with insertting usename
print("Welcome to Movie Mayham!")
username = input("Please enter a username: ")

print(f"Hi {username}! let's get started")

#defining the questions from our json file
file_path = "Ques.json"

def load_questions(file_path):
    with open(file_path, 'r') as file: #with definiing file path to "file" it's able to take the json
        questions = json.load(file)     #file and open in read mode 
    return questions

#going to run quiz in this function
#score is gonna be the start of how many questions and after every question correct
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
            if answer.isdigit():
                answer_index = int(answer) - 1
                if 0 <= answer_index < len(item['options']):
                    inputted_answr = item['options'][answer_index]
                    correct_answr = item['answer']

                    if inputted_answr == correct_answr:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is {correct_answr}")
                else:
                    print("INVALID sorry")

print(f"Your final socre {username} is [score]")

questions = load_questions(file_path)
run_quiz(questions)