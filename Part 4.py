# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20210372
# Date: 06.12.2021

print("Staff version with list of accessed data from the text file!\n")
# declaring variables and assigning initial values
total = 0
count_progress = 0
count_trailer = 0
count_retriever = 0
count_exclude = 0
# declaring empty lists
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []


# defining a function for vertical histogram
def vertical_histogram():
    # calculating the total progression outcomes
    total_outcomes = count_progress + count_trailer + count_retriever + count_exclude
    print('-' * 60)
    print('Vertical Histogram.\n')
    header = ["Progress", str(count_progress), "|", " Trailer", str(count_trailer), "|", " Retriever",
              str(count_retriever), "|", "Exclude", str(count_exclude)]
    print(' '.join(header))
    for x in range(total_outcomes):
        print("    {0}            {1}            {2}           {3}".format(
            '*' if x < count_progress else ' ',
            '*' if x < count_trailer else ' ',
            '*' if x < count_retriever else ' ',
            '*' if x < count_exclude else ' ',
        ))
    print(total_outcomes, 'outcomes in total.')
    print('-' * 60)


# asking the user to input the credits at pass, defer and fail.
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
    if total_credits != 120:  # check the total of the credits, if it's not equal to 120, loop iterates
        print("Total incorrect")
        continue

    else:
        # declaring the progression outcomes
        if pass_credits == 120:
            print("Progress")
            count_progress += 1
            # if the progression outcome is "Progress", the progress_list appends the pass, defer and fail credits to it.
            progress_list.append([pass_credits, defer_credits, fail_credits])

        elif pass_credits == 100:
            print("Progress(module trailer)")
            count_trailer += 1
            # if the progression outcome is "Progress(module trailer)", the trailer_list appends the pass, defer and fail credits to it.
            trailer_list.append([pass_credits, defer_credits, fail_credits])

        elif pass_credits == 80 or pass_credits == 60:
            print("Do not progress- module retriever")
            count_retriever += 1
            # if the progression outcome is "Do not progress- module retriever", the retriever_list appends the pass, defer and fail credits to it.
            retriever_list.append([pass_credits, defer_credits, fail_credits])

        elif pass_credits == 40:
            if defer_credits == 0:
                print("Exclude")
                count_exclude += 1
                # if the progression outcome is "Exclude", the exclude_list appends the pass, defer and fail credits to it.
                exclude_list.append([pass_credits, defer_credits, fail_credits])
            else:
                print("Do not progress- module retriever")
                count_retriever += 1
                retriever_list.append([pass_credits, defer_credits, fail_credits])

        elif pass_credits == 20:
            if defer_credits == 0:
                print("Exclude")
                count_exclude += 1
                exclude_list.append([pass_credits, defer_credits, fail_credits])
            elif defer_credits == 20:
                print("Exclude")
                count_exclude += 1
                exclude_list.append([pass_credits, defer_credits, fail_credits])

            else:
                print("Do not progress- module retriever")
                count_retriever += 1
                retriever_list.append([pass_credits, defer_credits, fail_credits])

        elif pass_credits == 0:
            if defer_credits == 40:
                print("Exclude")
                count_exclude += 1
                exclude_list.append([pass_credits, defer_credits, fail_credits])

            elif defer_credits == 20:
                print("Exclude")
                count_exclude += 1
                exclude_list.append([pass_credits, defer_credits, fail_credits])

            elif defer_credits == 0:
                print("Exclude")
                count_exclude += 1
                exclude_list.append([pass_credits, defer_credits, fail_credits])

            else:
                print("Do not progress- module retriever")
                count_retriever += 1
                retriever_list.append([pass_credits, defer_credits, fail_credits])
        # asking the user whether he wants to another set of data.
        while True:
            option = input(
                "\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:  ").lower()
            if option == 'y':
                break
            elif option == 'q':  # if the user quits the program it prints the horizontal histogram
                vertical_histogram()
                break
            else:
                print(
                    "Option is not recognized. Please enter a valid input.")  # if the option is not 'q' or 'y', the
                # loop iterates until a valid input is given
                continue

    if option == 'y':  # user wants to add another set of data so the loop continues
        continue
    else:
        break
    break

# writing the lists to a text file; credit_file.txt
file = open("credit_file.txt", 'w')
for i in range(len(progress_list)):
    file.write('Progress -')  # write to the credit file.
    file.write(str(progress_list[i]))
    file.write('\n')
for i in range(len(trailer_list)):
    file.write('Progress (Module Trailer)-')
    file.write(str(trailer_list[i]))
    file.write('\n')
for i in range(len(retriever_list)):
    file.write('Module Retriever -')
    file.write(str(retriever_list[i]))
    file.write('\n')
for i in range(len(exclude_list)):
    file.write('Exclude -')
    file.write(str(exclude_list[i]))
    file.write('\n')
file.close()  # closing the credit file

print("\nReading user inputs from the credit file.\n")
# opens the credit_file.txt and reads the stored data
try:
    file1 = open("credit_file.txt", 'r')
    lines = file1.readlines()  # returns a list of each line in the file
    for line in lines:
        print(line)
    file.close()
except FileNotFoundError:
    print("File not found")  # error is encountered if the file is not found .
