# Given the input of a student number, generate two integers 
# indicating the questions that a student needs to answer.
# 

def generate_numbers(a_student_id, num_questions):
    # Remove any non-numeric characters
    id = ''.join(filter(str.isdigit, a_student_id))

    # Check that the student ID is valid (8 digits)
    if len(id) != 8:
        raise ValueError("Invalid student ID: it should be 8 digits")
    
    # Use a simple algorithm to generate two distinct numbers from 1 to num_questions
    sum_digits = sum(int(digit) for digit in id)
    first = (sum_digits % 7) + 1

    # Calculate the second number using the product of the digits
    product = 1
    for digit in id:
        if (int(digit) != 0):
            product *= int(digit)
    second = (product % 7) + 1

    while first == second:
        second = (second % 7) + 1
    
    return first, second


try:
    N_QUESTIONS = 10
    student_id = input("Enter your student ID (XXX-XX-XXX): ")
    num1, num2 = generate_numbers(student_id, N_QUESTIONS)
    print (f"Your two assignments are {num1} and {num2}")
except ValueError as e:
    print(f"Error {e}")