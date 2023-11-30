print("Progression outcomes of Students.\n")

# declaring variables and assigning initial values
total = 0

outComeCount = {"Progress": 0,"Trailer": 0,"Retriever": 0,"Exclude": 0}

# defining a function for horizontal histogram
def horizontal_histogram():
    print('-' * 60)
    print('Horizontal Histogram.\n')
    print('Progress  ', outComeCount["Progress"], ':', '*' * outComeCount["Progress"])
    print('Trailer   ', outComeCount["Trailer"], ':', '*' * outComeCount["Trailer"])
    print('Retriever ', outComeCount["Retriever"], ':', '*' * outComeCount["Retriever"])
    print('Exclude   ', outComeCount["Exclude"], ':', '*' * outComeCount["Exclude"], '\n')
    # calculating the total number of progression outcomes
    total_outcomes = sum(list(outComeCount.values()))
    print(total_outcomes, 'outcomes in total.')
    print('-' * 60)

def validation(prompt):
    while True:
        try:
            credit = input(prompt)
            if credit.strip() == "":
                prompt("Please enter a value")
            elif int(credit) not in range(0,121,20):
                print("Out of range")
            else: 
                return int(credit)
        except ValueError:
            print("Integer required!")
        
def Outcome(pass_credit,defer_credit,fail_credit):
    if pass_credit == 120:
            output = "Progress"
    elif (pass_credit+defer_credit) < fail_credit:
            output = "Exclude"
    elif pass_credit == 100 and (defer_credit==20 or fail_credit==20):
            output = "Trailer"
    elif (pass_credit in [0,20,40,60,80]) and (defer_credit in [0,20,40,60,80,100,120]) and (fail_credit in [0,20,40,60]):
            output = "Retriever"
    return output

# defining a function for student version
def student_version():
    while True:   
        pass_credit = validation("Enter your credits at Pass: ")
        defer_credit = validation("Enter your credits at Defer: ")
        fail_credit = validation("Enter your credits at Fail: ")

        total_credits = pass_credit + defer_credit + fail_credit
        if total_credits != 120:
            print("Total incorrect")
            continue
        print(Outcome(pass_credit,defer_credit,fail_credit))
        break

# defining a function for the staff use
def staff_version():
     while True:
        pass_credit = validation("Enter your credits at Pass: ")
        defer_credit = validation("Enter your credits at Defer: ")
        fail_credit = validation("Enter your credits at Fail: ")

        total_credits = pass_credit + defer_credit + fail_credit
        if total_credits != 120:
            print("Total incorrect")
            continue

        result = Outcome(pass_credit,defer_credit,fail_credit)
        outComeCount[result] += 1
        userChoice = str(input("Would you like to enter another set of data (y/n): ")).strip()
        if userChoice.lower() == "n":
             break

while True:
    try:
        # figuring out what version should be continued.
        version = int(input("Enter 1 for Staff use and 2 for Student use: "))
        if version == 1:
            print("\nStaff version with Histogram.")
            staff_version()
            break
        elif version == 2:
            print("\nStudent version.")
            student_version()
            break
        else:  # if the user enter a version other than 1 and 2, the loop continues until 1 or 2 is entered
            print(version, " not recognized. Please enter 1 or 2! ")
            continue
    except ValueError:
        # if the user input a string, loop continues until a integer value is given
        print("Integer required")
