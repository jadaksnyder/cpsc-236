import random
import time
import os

def get_student_info():
    attempts = 0
    while attempts < 3:
        first_name = input("Enter your First name: ")
        last_name = input("Enter your Last name: ")
        student_id = input("Enter your ID (A followed by 5 digits): ")
        if validate_id(student_id):
            return first_name, last_name, student_id
        else:
            print("Invalid ID. Please enter a valid ID.")
            attempts += 1
    print("You've exceeded the maximum number of attempts. Exiting.")
    exit()

def validate_id(student_id):
    if len(student_id) != 6:
        return False
    if student_id[0] != 'A':
        return False
    if not student_id[1:].isdigit():
        return False
    return True

def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            question, options, answer = line.strip().split(';')
            questions.append({'question': question, 'options': options.split(','), 'answer': answer})
    return questions

def get_unique_questions(questions, num_questions):
    return random.sample(questions, num_questions)

def display_question(question, index):
    print(f"\nQuestion {index + 1}: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{chr(65 + i)}. {option}")

def get_answer():
    while True:
        user_answer = input("Your answer (A, B, C, or D): ").upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            return user_answer
        else:
            print("Invalid answer. Please enter A, B, C, or D.")

def take_quiz(questions):
    start_time = time.time()
    answers = []
    for index, question in enumerate(questions):
        display_question(question, index)
        answer = get_answer()
        answers.append({'question': question['question'], 'correct_answer': question['answer'], 'user_answer': answer})
    end_time = time.time()
    elapsed_time = end_time - start_time
    return answers, elapsed_time

def calculate_score(answers, num_questions):
    correct_answers = sum(1 for answer in answers if answer['correct_answer'] == answer['user_answer'])
    if num_questions == 10:
        return correct_answers
    elif num_questions == 20:
        return correct_answers / 2

def generate_student_file(first_name, last_name, student_id, score, elapsed_time, answers):
    filename = f"{student_id}_{first_name}_{last_name}.txt"
    with open(filename, 'w') as file:
        file.write(f"Student ID: {student_id}\n")
        file.write(f"First name: {first_name}\n")
        file.write(f"Last name: {last_name}\n")
        file.write(f"Score: {score}\n")
        file.write(f"Elapsed time: {elapsed_time:.2f} seconds\n\n")
        file.write("Question\tCorrect Answer\tYour Answer\n")
        for index, answer in enumerate(answers):
            file.write(f"{index + 1}\t{answer['correct_answer']}\t\t{answer['user_answer']}\n")
    print(f"Results saved in {filename}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Welcome to the Quiz Maker!")
    first_name, last_name, student_id = get_student_info()
    questions = load_questions('testbank.xlsx')
    
    while True:
        clear_screen()
        print("\nQuiz Maker\n")
        print("1. Take 10-question quiz")
        print("2. Take 20-question quiz")
        print("3. Exit")
        option = input("Choose an option: ")
        if option == '1':
            num_questions = 10
        elif option == '2':
            num_questions = 20
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")
            continue

        #unique_questions = get_unique_questions(questions, num_questions)
        #answers, elapsed_time = take_quiz(unique_questions)
        #score = calculate_score(answers, num_questions)
        #generate_student_file(first_name, last_name, student_id, score, elapsed_time, answers)

        choice = input("\nEnter Q to exit or S to start a new quiz: ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice == 'S':
            continue
        else:
            print("Invalid choice. Exiting.")
            break

if __name__ == "__main__":
    main()