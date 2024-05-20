def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Your name")
    print("Student name:", student_name)

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score_input = input("Enter your math score ")
    math_score = float(math_score_input)
    print("Math score:", math_score)

    science_score_input = input("Enter your Science score")
    science_score = float(science_score_input)
    print("Science score:", science_score)

    english_score_input = input("Enter your English score")
    english_score = float(english_score_input)
    print("English score:", english_score)

    # Calculate the average grade
    average_grade = ((math_score + science_score + english_score) / 3.0)
    print("Average grade:", average_grade)

    # Return the student's name and their average grade
    return student_name, average_grade


if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(student_name, f"Average Grade", average_grade) 