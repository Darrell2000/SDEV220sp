""" Darrell Davis"""
"""Module 2 Lab - Case Study: if...else and while"""
"""3/26/2025"""

# Writing a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. 

# Python app to check if a student qualifies for the Dean's List or Honor Roll

# Run in a loop to accept multiple student records
while True:
    # Get the student's last name
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    
    # Check if the user wants to stop the program
    if last_name.upper() == 'ZZZ':
        print("Exiting the program. Goodbye!")
        break

    # Get the student's first name
    first_name = input("Enter the student's first name: ")

    # Get and validate the student's GPA
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue

    # Display the student's full name and GPA
    print(f"\nStudent: {first_name} {last_name} | GPA: {gpa}")
    
    # Check for Dean's List eligibility
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    # Check for Honor Roll eligibility
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")
    
    print("-" * 40)  # Separator for readability

# Python app to test if students qualify for the Dean's List or Honor Roll
# Using sample data for five students

# Sample list of students (first name, last name, GPA)
students = [
    ("John", "Smith", 3.6),
    ("Lisa", "Brown", 3.3),
    ("Kevin", "Lee", 3.1),
    ("Amy", "Lee", 3.5),
    ("Raj", "Patel", 3.25)
]

# Loop through each student in the sample list
for first_name, last_name, gpa in students:
    print(f"\nStudent: {first_name} {last_name} | GPA: {gpa}")

    # Check for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    # Check for Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    # Neither
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")

    print("-" * 40)  # Separator line for readability
