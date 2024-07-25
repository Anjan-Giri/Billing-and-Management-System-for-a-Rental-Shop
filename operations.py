#importing different files and functions
import datetime
from read import read_equipments
from write import update_file, return_update_file

today = datetime.datetime.now() #calling function from datetime in today variable
items = read_equipments() #calling function from read in items

# Initializing the variables before using them
equip_name = ""  
equip_brand = ""
equip_price = 0.0
equip_quantity = 0
name_ = ""
num_ = ""
email_ = "" 
quan_ = 0
days_ = 0

#defining a function
def select1():
    """
    this function reads the equipments.txt file and
    it displays the content of the file in a systematic way
    """

    #printing the message above the equipments
    print("------------------------------------------------------------------------------------------------")
    print("Here are the list of the items")
    print("------------------------------------------------------------------------------------------------")
    print("S.N \t Equipments \t\t Brand \t\t     Price per 5 days    Num of available items")
    print("------------------------------------------------------------------------------------------------")

    #opening the equipments file
    file = open("equipments.txt","r")

    a = 0
    #using for loop to get the values from the file
    for i in file:
        l_ = i.strip().split(",")
            
        equipment = l_[0]
        brand = l_[1]
        price = l_[2]
        quantity = l_[3]

        a = a+1

        #displaying values in a systematic way    
        if a == 1:
            print(f" {a}    {equipment} \t{brand} \t\t {price} \t\t\t{quantity}")
        elif a == 2:
            print(f" {a}    {equipment} \t\t{brand} \t {price} \t\t\t{quantity}")
        elif a == 3:
            print(f" {a}    {equipment} \t\t{brand} \t\t {price} \t\t\t{quantity}")
        elif a == 4:
            print(f" {a}    {equipment} \t{brand} \t\t\t {price} \t\t\t {quantity}")
        elif a == 5:
            print(f" {a}    {equipment} \t\t{brand} \t {price} \t\t\t{quantity}")
                
    print("------------------------------------------------------------------------------------------------")
    file.close() #closing the file

#defining a function      
def rent_items():

    """
    this function performs all tasks related to renting the equipment
    it validates user input and reads them
    it check all the conditions necessary
    it runs the program in loop until the loop is ended due to a ending option
    """
    loop = True #setting value of loop to True
    #using while loop to run the code in loop
    while loop == True:
        #using try to ensure that valid input is entered
        try:
            #taking input from user
            cid = int(input("Enter the number corresponding to the equipment you want to rent(1-5): "))
            if 6 > cid > 0: #checking the condition
                #using for loop to display the selected item from dictionary
                for id in items:
                    print(items[cid])                   
                    break #ending for loop
                #using try to ensure that valid input is entered
                try:
                    #taking input from user
                    quan_ = int(input("Enter quantity of the equipment that you would like to rent: "))
                    days_ = int(input("Number of days you are renting this equipment for: "))
                    
                    if quan_ != "" and days_ != "": #checking the condition

                        option2 = True #setting value of option2 to True
                        #using while loop to run the code in loop
                        while option2 == True:

                            #taking input from user    
                            ans_ = input(" Press 'Enter' if you are done! \n Type any key if you want to rent more items!")

                            #checking the condition
                            if ans_ == "":
                                #taking inputs from the user
                                num_ = input("Enter your contact number: ")
                                email_ = input("Enter your email address: ")
                                name_ = input("Enter your name: ")

                                #checking the condition
                                if name_ != "" and num_ != "" and email_ != "":
                                    print("----------------------")
                                    print("Equipment rented successfully!") #displaying success message
                                    print("----------------------")
                                    
                                    option2 = False #ending the loop
                                    loop = False #ending the loop
                                #when condition is not matched in if    
                                else:
                                    print("Please enter all required details to rent the item!")
                            #when condition is not matched in if        
                            else:

                                items_ = select1() #calling the select1 function
                                again = rent_items() #calling the rent_items function
                    #when condition is not matched in if            
                    else:
                        print("Please enter all data!")
                #when invalid input is entered        
                except:
                    print("Enter valid dataaaaaaaa!")
            #when condition is not matched in if        
            else:
                print("Enter a valid id!")
        #when invalid input is entered        
        except:
            print("Enter valid data!")
    rent_details(cid,quan_,days_,name_,num_,email_)
    update_file(cid, quan_)
    return int(cid), quan_, days_, name_, num_, email_  #returning the values
    

#defining a function
def rent_details(cid, quan_, days_, name_, num_, email_):
    """
    this function is used to write a file
    it generates a txt file with invoice in it
    the invoice contains all the details about the purchase made
    """
   
    equip_name = items[cid][0:] #accessing value from dictionary
    equip_brand = items[cid][1:]
    equip_price = items[cid][2:]
    equip_quantity = items[cid][3:]
            
    equip_price_ = equip_price[0].replace('$','') #replacing $ sign in the price with empty string
    total_price = int(equip_price_)/5 * quan_ * days_ #calculating the total price
    #storing all purchase details in rent_details
    rent_details = "\n Equipment ID: " + str(cid) + "\n Equipment name: " + equip_name[0] + "\n Equipment brand: " + equip_brand[0] + "\n Equipment Price: " + str(equip_price[0]) + "\n Number of equipment: " + str(equip_quantity[0]) + "\n Number of equipment rented: " + str(quan_) + "\n Number of days it is rented for: " + str(days_) + "\n-------------------------------------------""\n Customer's Name: " + name_ + "\n Contact Number: " + num_ + "\n Email Address: " + email_ + "\n-------------------------------------------""\n Total Price: $" + str(total_price) + "\n-------------------------------------------"    
    print(rent_details) #displaying all purchase details
    
    #generating a invoive file with all purchase details in it along with date, time, store name and its location
    file = open(str(name_) + str(num_) + ".txt","w")
    file.write("-------------------------------------------")
    file.write("\n\t\t" +str(today))
    file.write("\n------------------------------------------")
    file.write("\n\t\t  FullMarks Rental Store \t")
    file.write("\n------------------------------------------")
    file.write("\n\t\t Machhapokhari, Kathmandu \t")
    file.write("\n------------------------------------------")
    file.write("\n\t\t\tPurchase Details: ")
    file.write("\n------------------------------------------")
    file.write("\n\t\t" + rent_details)



#defining a function    
def select2():
    """
    this function reads the equipments.txt file and
    it displays the name and brand content of the file in a systematic way
    """

    #printing the message above the equipments
    print("-------------------------------------------------")
    print("Choose equipment to return")
    print("-------------------------------------------------")
    print("S.N \t Equipment to return \t\t Brand")
    print("-------------------------------------------------")

    #opening the equipments file
    file = open("equipments.txt","r")

    a = 0
    #using for loop to get the values from the file
    for i in file:
        l_ = i.strip().split(",")

        equipment = l_[0]
        brand = l_[1]

        a = a+1

        #displaying values in a systematic way    
        if a == 1:
            print(f" {a}    {equipment} \t{brand}")
        elif a == 2:
            print(f" {a}    {equipment} \t\t{brand}")
        elif a == 3:
            print(f" {a}    {equipment} \t\t{brand}")
        elif a == 4:
            print(f" {a}    {equipment} \t{brand}")
        elif a == 5:
            print(f" {a}    {equipment} \t\t{brand}")
                
    print("-------------------------------------------------")
    file.close() #closing the file
    
#defining a function
def return_items(naam_, extra_, extra_fee, number_):
    """
    this function performs all tasks related to returning the equipment
    it validates user input and reads them
    it check all the conditions necessary
    it runs the program in loop until the loop is ended due to a ending option
    """
    r = True #setting value of r to true
    #using while loop to run the code in a loop
    while r == True:
        #using try to ensure that valid input is entered
        try:
            #taking input from user
            return_ = int(input("Enter the number corresponding to the equipment you want to return(1-5): "))
            if 0 < return_ < 6: #checking the condition
                #using for loop to display the selected item from dictionary
                for id in items:
                    print(items[return_])                   
                    break #ending for loop
                s = False #setting value of s to false
                #using while loop to run the code in loop
                while s == False:
                    #using try to ensure that valid input is entered
                    try:
                        #taking input from the user
                        return_quan = int(input("Enter the number of selected equipment that you want to return: "))
                        if return_ == 1: #checking the condition
                            return__ = input("Has it been rented for extra days (yes/no): ") #taking input from the user
                            if return__ == "yes": #checking the condition
                                price = 8
                                #taking inputs from the user
                                extra_ = int(input("Enter number of extra days: "))
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                extra_fee = ((price/5) * extra_) * 2 #calculating the extra_fee
                                #displaying user entered details
                                print("-------------------------------")
                                print("As you failed to return the equipment before your designated day,\n Your FINE is: $",extra_fee)
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                
                            elif return__ == "no": #checking the condition
                                #taking inputs from the user
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                #displaying user entered details
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                                    
                        elif return_ == 2: #checking the condition
                            return__ = input("Has it been rented for extra days (yes/no): ")
                            if return__ == "yes": #checking the condition
                                price = 189
                                #taking inputs from the user
                                extra_ = int(input("Enter number of extra days: "))
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                extra_fee = ((price/5) * extra_) * 2 #calculating extra_fee
                                #displaying user entered details
                                print("-------------------------------")
                                print("As you failed to return the equipment before your designated day,\n Your FINE is: $",extra_fee)
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                
                            elif return__ == "no": #checking the condition
                                #taking inputs from the user
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                #displaying user entered details
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                                    
                        elif return_ == 3: #checking the condition
                            return__ = input("Has it been rented for extra days (yes/no): ")
                            if return__ == "yes":
                                price = 322
                                #taking inputs from the user
                                extra_ = int(input("Enter number of extra days: "))
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                extra_fee = ((price/5) * extra_) * 2 #calculating extra_fee
                                #displaying user entered details
                                print("-------------------------------")
                                print("As you failed to return the equipment before your designated day,\n Your FINE is: $",extra_fee)
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                
                            elif return__ == "no": #checking the condition
                                price = 322
                                #taking inputs from the user
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                #displaying user entered details
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                                    
                        elif return_ == 4: #checking the condition
                            return__ = input("Has it been rented for extra days (yes/no): ")
                            if return__ == "yes":
                                price = 489
                                #taking inputs from the user
                                extra_ = int(input("Enter number of extra days: "))
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                extra_fee = ((price/5) * extra_) * 2 #calculating extra_fee
                                #displaying user entered details
                                print("-------------------------------")
                                print("As you failed to return the equipment before your designated day,\n Your FINE is: $",extra_fee)
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                
                            elif return__ == "no": #checking the condition
                                #taking inputs from the user
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                #displaying user entered details
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                                    
                        elif return_ == 5: #checking the condition
                            return_ = input("Has it been rented for extra days (yes/no): ")
                            if return__ == "yes":
                                price = 344
                                #taking inputs from the user
                                extra_ = int(input("Enter number of extra days: "))
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                extra_fee = ((price/5) * extra_) * 2 #calculating extra_fee
                                #displaying user entered details
                                print("-------------------------------")
                                print("As you failed to return the equipment before your designated day,\n Your FINE is: $",extra_fee)
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                
                            elif return__ == "no": #checking the condition
                                #taking inputs from the user
                                naam_ = input("Enter customer's name: ")
                                number_ = input("Enter your contact number: ")
                                #displaying user entered details
                                print("-------------------------------")
                                print("Customer's name: " + naam_)
                                print("-------------------------------")
                                print("Customer's number: " + number_)
                                print("-------------------------------")
                                more = input("Press 'Enter' to return more items. Press any key to end.")
                        #when condition is not matched in if         
                        else:
                            print("please enter a valid id")
                    #when invalid input is entered        
                    except:
                        print("enter a valid input")
                    s = True #ending the loop
                
                    
                if more == "": #checking the condition         
                    items__ = select2()
                    items___ = return_items()
                #when condition is not matched in if     
                else:
                    print("Thank you for visiting FullMarks Rental Store!!")
                    r = False #ending the loop   
            #when condition is not matched in if         
            else:
                print("Please enter a valid numbeeeeeer!")
        #when invalid input is entered        
        except:
            print("Please enter a valid number!")   
    
    return_update_file(return_, return_quan)
    return_details(return_, return_quan, naam_, extra_, extra_fee, number_) 
    return int(return_), return_quan, naam_, extra_, extra_fee, number_ #returning the values

#defining a function
def return_details(return_, return_quan, naam_, extra_, extra_fee, number_):
    """
    this function is used to write a file
    it generates a txt file with invoice in it
    the invoice contains all the details about the return transaction
    """
    return_equip_name = items[return_][0:]#accessing value from dictionary
    return_equip_brand = items[return_][1:]

    #storing all details about the return transaction done in return_details
    return_details = "Returned Equipment: " + return_equip_name[0] + "\nEquipment Brand: " + return_equip_brand[0] + "\nQuantity of equipment returned: " + str(return_quan) + "\nCustomer's name: " + naam_ + "\nContact: " + number_ + "\n-------------------------------------------""\nNumber of extra days: " + str(extra_) + "\nFine for being late: " + str(extra_fee) + "\n-------------------------------------------"
    print(return_details) #displaying all details

    #generating a invoive file with all return details in it along with date, time, store name and its location
    file = open(str(naam_) + str(number_) + ".txt","w")
    file.write("-------------------------------------------")
    file.write("\n\t\t" +str(today))
    file.write("\n------------------------------------------")
    file.write("\n\t\t  FullMarks Rental Store \t")
    file.write("\n------------------------------------------")
    file.write("\n\t\t Machhapokhari, Kathmandu \t")
    file.write("\n------------------------------------------")
    file.write("\n\t\t\tReturn Details: ")
    file.write("\n------------------------------------------")
    file.write("\n" + return_details)
