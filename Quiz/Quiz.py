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
                                        #Below checks the "options" key and puts items into an index to start from 1 instead of 0
        if 'options' in item:
            for idx, option in enumerate(item['options'], start=1):
                print(f"{idx}. {option}")

            answer = input("Your answer: ")
            
            #checking to see it the answer is correct
            if answer.isdigit():                    #Since we are using #'s for answers this takes the 
                answer_index = int(answer) - 1      #string input to an int and adjusts it for zero-base index
                if 0 <= answer_index < len(item['options']):        #This line makes sure the options chosen are less than
                    inputted_answr = item['options'][answer_index]  #the length of options we have for it to be valid
                    correct_answr = item['answer']

                    if inputted_answr == correct_answr:
                        print("Correct!")
                        score += 1  #If anyswer is correct it will add 1 to your score
                    else:
                        print(f"Wrong! The correct answer is {correct_answr}")
                else:
                    print("INVALID sorry")

    print(f"Your final socre {username} is {score}!") #prints final socre along with username

questions = load_questions(file_path) 
run_quiz(questions)         ##Loads all my questions and commands