def calculate_gpa():
    # Get the student's name
    name = input("What is your name: ")

    # Get the grades for each course
    Course1 = float(input(f"Please enter your Mathematics Note {name}: "))
    Course2 = float(input(f"Please enter your Science Note {name}: "))
    Course3 = float(input(f"Please enter your Geography Note {name}: "))
    Course4 = float(input(f"Please enter your Biology Note {name}: "))
    Course5 = float(input(f"Please enter your History Note {name}: "))

    # Function to calculate GPA
    def gpa(a, b, c, d, e):
        return (a + b + c + d + e) / 5

    # Calculate GPA
    gpa_result = gpa(Course1, Course2, Course3, Course4, Course5)
    print(f"{name}, your GPA is: {gpa_result}")

    # Function to assign a prize based on GPA
    def assign_prize(gpa_result):
        if 19 <= gpa_result <= 20:
            return "PS5"
        elif 18 <= gpa_result < 19:
            return "Smartwatch"
        elif 17 <= gpa_result < 18:
            return "Bicycle"
        else:
            return "Unfortunately, you did not win a Prize."

    # Assign prize using the function
    prize = assign_prize(gpa_result)

    # Display the prize
    print(f"{name}, your Prize is: {prize}")


# Main loop
while True:
    calculate_gpa()
    repeat = input("Would you like to calculate GPA again? Type 'yes' to continue or 'no' to exit: ").strip().lower()
    if repeat == "no":
        print("Have a nice day!")
        break
