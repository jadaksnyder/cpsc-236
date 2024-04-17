import time
import random
import csv


def validate_ID(): #Tyler created this function
    attempts = 0
    first_name = str(input("Please enter your first name: "))
    last_name = str(input("Please enter your last name: "))
    while attempts <= 2: #attempts is initialized at 0, so the program will run a maximum of three times until the user enters valid input
        ID = input(
            "Please enter your student ID: "
        )  # making sure length of the ID is equal to 6
        if len(ID) != 6:
            print("Please enter a valid student ID.")
        elif not ID.startswith("A"):  # must start with a capital A
            print("Please enter a valid ID.")
        elif (
            int(ID[1:]) < 1 or int(ID[1:]) > 99999
        ):  # return all elements starting at index 1
            print("Please enter a valid student ID.")
        else:
            return first_name, last_name, ID
        attempts += 1 #this increases the value of "attempts" by 1
    print("You've exceeded the maximum number of attempts. Exiting the program.")
    exit()


def load_unique_questions(filename, num_questions): #Jada created this function
    filename = "testbank.csv"
    with open(filename) as file:
        csv_reader = csv.DictReader(file) #use DictReader() to convert each row in the CSV file into a dictionary, so we can access those values by the column names
        rows = list(csv_reader)
        if num_questions == 10:
            random_questions = random.sample(rows, 10) #use random.sample to get 10 random questions out of the csv file
        else:
            random_questions = random.sample(rows, 20) #use random.sample to get 20 random questions out of then csv file
        return random_questions


def check_for_valid_answer(): #Tyler created this function
    while True: #use a while loop so that the program will run until the user types in a valid answer
        answer = input("Please enter your answer (A, B, or C): ").upper()
        if answer not in ["A", "B", "C"]: #use an if statement to ensure the user inputs a valid answer
            print("Please enter a valid answer (A, B, or C)")
        else:
            return answer


def calculate_score(questions, answers, num_questions): #Jada created this function
    if num_questions == 10: #use if statements to initialize the weight of each quiz
        question_weight = 1
    elif num_questions == 20:
        question_weight = 0.5
    else:
        raise ValueError("Invalid number of questions.") #raise ValueError is used if the value of "num_questions" does not match either of the conditions
    score = 0
    for question, answer in zip(questions, answers): # "Zip" is used to pair a question from "questions" and an answer from the "answers" list
        if answer == question["Answer"]:
            score += question_weight 
    return score


def create_student_file( #Jada created this function
filename, first_name, last_name, ID, score, elapsed_time, questions, answers):
    with open(filename, "w") as file: #use "w" to write a new txt file for the student
        file.write(f"Student ID: {ID}\n") #we will also use f strings to input the values from the test into the new txt file
        file.write(f"First Name: {first_name}\n")
        file.write(f"Last Name: {last_name}\n")
        file.write(f"Score: {score}\n")
        file.write(f"Elapsed time: {elapsed_time}\n")
        file.write(f"Quiz questions and answers:\n")
        for question, answer in zip(questions, answers): #Again, use "zip" to pair the questions and the answers
            file.write(f"Question: {question['question']}\n")
            file.write(f"Correct Answer: {question['Answer']}\n")
            file.write(f"Student's answer: {answer}\n")



def take_quiz(): #Tyler and Jada worked on this together
    filename = "testbank.csv" #input the csv file
    num_questions = input("Please choose the number of questions (10 or 20): ")
    if num_questions.isdigit(): #use an if statement to make sure the user enters "10" or "20". If not, the quiz will default to ten questions
        num_questions = int(num_questions)
        if num_questions not in [10, 20]:
            print("Invalid choice. Defaulting to 10.")
            num_questions = 10
    else:
        print("Invalid input. Defaulting to 10.")
        num_questions = 10


    student_data = validate_ID() #incorporate the validateID() function 
    first_name, last_name, ID = student_data
    questions = load_unique_questions(filename, num_questions) #load the questions
    user_answers = []

    question_number = 1
    
    time_limit = 600 #set the time limit for the user

    start_time = time.time()
    for question in questions: #This loop iterates over each question in the dictionary and prints out the question number and total number of questions.
        print(f"Question {question_number} / {len(questions)}:", question["question"])
        print("Options:")
        print("A:", question["Option A"])
        print("B:", question["Option B"])
        print("C:", question["Option C"])
        
        user_answer = check_for_valid_answer()
        user_answers.append(user_answer)
        question_number += 1

        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit: #use an if statement to exit the program once the time limit is up
            print("Time's up! You have exceeded the time limit.")
            break

    score = calculate_score(questions, user_answers, num_questions)
    create_student_file(f"{ID}_{first_name}_{last_name}.txt",
        first_name,
        last_name,
        ID,
        score,
        elapsed_time,
        questions,
        user_answers,)
    
    print("Quiz completed!")
    print(f"Your score: {score}/{len(questions)}")
    print(f"Elapsed time: {elapsed_time} seconds")

def main(): #Tyler created this function
    while True: #use a while loop so that the program keeps looping until the user inputs whether they want to take the quiz again or not
        take_quiz()
        choice = input("\nEnter Q to exit or any other key to start a new quiz: ").upper()
        if choice == "Q":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()