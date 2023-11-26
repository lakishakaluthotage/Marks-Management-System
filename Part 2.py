print("Staff version with Vertical Histogram.\n")

#declaring variables and assigning initial values
total=0
count_progress=0
count_trailer=0
count_retriever=0
count_exclude=0


#defining a function for vertical histogram
def vertical_histogram():
                
        total_outcomes=count_progress + count_trailer + count_retriever + count_exclude
        print('-'*60)
        print('Vertical Histogram.\n')
        header=["Progress | Trailer | Retriever | Exclude"]
        print(' '.join(header))
        for x in range(total_outcomes):
            print(" {0}           {1}         {2}          {3}".format(
                    '*' if x<count_progress   else ' ',
                    '*' if x< count_trailer   else ' ',
                    '*' if x< count_retriever else ' ',
                    '*' if x< count_exclude   else ' ',
                ))
        print(total_outcomes,'outcomes in total.')
        print('-'*60)

   

while True:
    #asking the user to input the credits at pass, defer and fail. 
    while True:
        try:
            pass_credits=int(input("Enter your credits at pass: "))
        except ValueError:
            print("Integer required")
            continue
        if pass_credits not in [20*i for i in range(7)]:
            print('Out of range')
        else:
            break
    while True:
        try:
            defer_credits=int(input("Enter your credits at defer: "))
        except ValueError:
            print("Integer required")
            continue
        if defer_credits not in [20*i for i in range(7)]:
            print('Out of range')
        else:
            break
    while True:
        try:
            fail_credits=int(input("Enter your credits at fail: "))
        except ValueError:
            print("Integer required")
            continue
        if fail_credits not in [20*i for i in range(7)]:
            print('Out of range')
        else:
            break
    #calculating the total number of progression outcomes
    total_credits= pass_credits + defer_credits +fail_credits
    if total_credits !=120:
        print("Total incorrect")
        continue
        
    else:
        #declaring the progression outcome.
        if pass_credits==120 :
            print("Progress")
            #if the progression outcome is progress,count_progress increases by 1.
            count_progress+=1
            

        elif pass_credits==100:
            print("Progress(module trailer)")
            #if the progression outcome is module trailer,count_trailer increases by 1.
            count_trailer+=1
            
            
        elif pass_credits==80 or pass_credits==60:
            print("Do not progress- module retriever")
            #if the progression outcome is module retriever,count_retriever increases by 1.
            count_retriever+=1
            
            
        elif pass_credits==40:
            if defer_credits==0:
                print("Exclude")
                #if the progression outcome is exclude,count_exclude increases by 1.
                count_exclude+=1
                
            else:
                print("Do not progress- module retriever")
                count_retriever+=1
                

        elif pass_credits==20:
            if defer_credits==0:
                print("Exclude")
                count_exclude+=1
                
            elif defer_credits==20:
                print("Exclude")
                count_exclude+=1
                
                
            else:
                print("Do not progress- module retriever")
                count_retriever+=1
                

        elif pass_credits==0:
            if defer_credits==40:
                print("Exclude")
                count_exclude+=1
                
                
            elif defer_credits==20:
                print("Exclude")
                count_exclude+=1
                
                
            elif defer_credits==0:
                print("Exclude")
                count_exclude+=1
                
                
            else:
                print("Do not progress- module retriever")
                count_retriever+=1
        #asking the user whether he wants to another set of data.
        while True:
                option= input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:  ").lower()
                if option == 'y':
                    break
                elif option== 'q':#if the user quits the program it prints the vertical histogram
                    vertical_histogram()
                    break
                else:
                    print("Option is not recognized. Please enter a valid input.")
                    continue
        
    if option=='y':#user wants to add another set of data so the loop iterates.
        continue
    else:
        break
                
                
    



