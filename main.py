#importing two files operations and write to use their functions in this file
import operations
import write

#printing welcome message of the store at the beginning of the program
print("-----------------------------------")
print("Welcome to FullMarks Rental Store")
print("-----------------------------------")
print("Select an option to perform required task: ")
       
option = True #setting value of option to true
#using while loop to run the code in a loop when the value of the option is true
while option == True:

    #printing message to ask the user for a input
    print("-------------------------------")
    print("Type 1 to rent ")
    print("-------------------------------")
    print("Type 2 to return ")
    print("-------------------------------")
    print("Type 3 to exit ")
    print("-------------------------------")

    #taking input from the user
    ans = input("Enter option as per your requirement: ")

    #when user enters an empty string
    if ans == "":
        print("Please enter a valid key! ")

    #when user enters 1 as a value
    elif ans == "1":

        #calling the functions from operations.py file
        operations.select1()
        operations.rent_items()
        operations.rent_details('cid', 'quan_', 'days_', 'name_', 'num_', 'email_')
        #calling the function from write.py file
        write.update_file('cid','quan_')

    #when user enters 2 as a value
    elif ans == "2":
        #calling the functions from operations.py file
        operations.select2()
        operations.return_items('naam_', 'extra_', 'extra_fee', 'number_')
        operations.return_details('return_', 'return_quan', 'naam_', 'extra_', 'extra_fee', 'number_')
        #calling the function from write.py file
        write.return_update_file('return_', 'return_quan')

    #when user enters 3 as a value
    elif ans == "3":
        print("You have exited") #printing exit message
        option = False #setting value of option to false to exit the loop
