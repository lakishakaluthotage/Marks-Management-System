# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 


print("Progression outcomes of Students.\n")

# declaring variables and assigning initial values
total = 0
count_progress = []
count_trailer = []
count_retriever = []
count_exclude = []


# defining a function for horizontal histogram
def horizontal_histogram():
    print('-' * 60)
    print('Horizontal Histogram.\n')
    # printing the histogram
    print('Progress  ', len(count_progress), ':', '*' * len(count_progress))
    print('Trailer   ', len(count_trailer), ':', '*' * len(count_trailer))
    print('Retriever ', len(count_retriever), ':', '*' * len(count_retriever))
    print('Exclude   ', len(count_exclude), ':', '*' * len(count_exclude), '\n')
    # calculating the total number of progression outcomes
    total_outcomes = len(count_progress) + len(count_trailer) + len(count_retriever) + len(count_exclude)
    print(total_outcomes, 'outcomes in total.')
    print('-' * 60)


# defining a function for student version
def student_version():
    while True:
        # ask the user to input credits at pass
        while True:
            try:
                pass_credits = int(input("Enter your credits at pass: "))
            except ValueError:
                print("Integer required")
                continue  # if the user input a string, program loops until the user inputs an integer
            if pass_credits not in [20 * i for i in range(7)]:  # check whether the inputs are in the relevant range
                print('Out of range')
            else:
                break
        # ask the user to input credits at defer
        while True:
            try:
                defer_credits = int(input("Enter your credits at defer: "))
            except ValueError:
                print("Integer required")
                continue
            if defer_credits not in [20 * i for i in range(7)]:
                print('Out of range')
            else:
                break
        # ask the user to input credits at fail
        while True:
            try:
                fail_credits = int(input("Enter your credits at fail: "))
            except ValueError:
                print("Integer required")
                continue
            if fail_credits not in [20 * i for i in range(7)]:
                print('Out of range')
            else:
                break
        # check whether the total of all the inputs is correct, if not the loop continues until the total is correct.
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            print("Total incorrect")
            continue

        # if the total is correct else block executes and gives the correct progression outcome.
        else:
            if pass_credits == 120:
                print("Progress")

            elif pass_credits == 100:
                print("Progress(module trailer)")


            elif pass_credits == 80 or pass_credits == 60:
                print("Do not progress- module retriever")


            elif pass_credits == 40:
                if defer_credits == 0:
                    print("Exclude")

                else:
                    print("Do not progress- module retriever")

            elif pass_credits == 20:
                if defer_credits == 0:
                    print("Exclude")

                elif defer_credits == 20:
                    print("Exclude")

                else:
                    print("Do not progress- module retriever")


            elif pass_credits == 0:
                if defer_credits == 40:
                    print("Exclude")

                elif defer_credits == 20:
                    print("Exclude")

                elif defer_credits == 0:
                    print("Exclude")

                else:
                    print("Do not progress- module retriever")
        break


# defining a function for the staff use
def staff_version():
    global pass_credits
    while True:

        while True:
            try:
                pass_credits = int(input("Enter your credits at pass: "))
            except ValueError:
                print("Integer required")
                continue
            if pass_credits not in [20 * i for i in range(7)]:
                print('Out of range')
            else:
                break
        while True:
            try:
                defer_credits = int(input("Enter your credits at defer: "))
            except ValueError:
                print("Integer required")
                continue
            if defer_credits not in [20 * i for i in range(7)]:
                print('Out of range')
            else:
                break
        while True:
            try:
                fail_credits = int(input("Enter your credits at fail: "))
            except ValueError:
                print("Integer required")
                continue
            if fail_credits not in [20 * i for i in range(7)]:
                print('Out of range')
            else:
                break
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            print("Total incorrect")
            continue


        else:
            # declaring the progression outcome
            if pass_credits == 120:
                print("Progress")
                count_progress.append(0)

            elif pass_credits == 100:
                print("Progress(module trailer)")
                count_trailer.append(0)


            elif pass_credits == 80 or pass_credits == 60:
                print("Do not progress- module retriever")
                count_retriever.append(0)


            elif pass_credits == 40:
                if defer_credits == 0:
                    print("Exclude")
                    count_exclude.append(0)
                else:
                    print("Do not progress- module retriever")
                    count_retriever.append(0)


            elif pass_credits == 20:
                if defer_credits == 0:
                    print("Exclude")
                    count_exclude.append(0)
                elif defer_credits == 20:
                    print("Exclude")
                    count_exclude.append(0)
                else:
                    print("Do not progress- module retriever")
                    count_retriever.append(0)


            elif pass_credits == 0:
                if defer_credits == 40:
                    print("Exclude")
                    count_exclude.append(0)
                elif defer_credits == 20:
                    print("Exclude")
                    count_exclude.append(0)
                elif defer_credits == 0:
                    print("Exclude")
                    count_exclude.append(0)
                else:
                    print("Do not progress- module retriever")
                    count_retriever.append(0)
            # asking the user whether he wants to another set of data
            while True:
                option = input(
                    "\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:  ").lower()
                if option == 'y':
                    break
                elif option == 'q':  # user quits the program,so it dispays the horizontal histogram and the total outcomes.
                    horizontal_histogram()
                    break
                else:
                    # if the option is not 'q' or 'y', the loop continues
                    print("Option is not recognized. Please enter a valid option.")
                    continue

        if option == 'y':  # user wants to add another set of data so the loop continues
            continue
        else:
            break
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
