#importing read_equipments function from read.py file
from read import read_equipments

#defining a function
def update_file(cid, quan_):
    """
    this function updates the equipments.txt file
    this function overwrites the details of the equipments
    it decreases the quantity of the equipment which is rented by how many items are rented
    """
    q = read_equipments() #calling the function in q
    total_quantity = q[cid][3] #getting quantity value from dictionary
    updated_quantity = int(total_quantity) - int(quan_) #calculating value of updated_quantity
    q[cid][3] = updated_quantity #storing the value in dictionary 

    #opening a file to rewrite it
    file = open("equipments.txt","w")

    #using for loop to update the value of quantity
    for value in q.values():
        file.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]))
        file.write("\n")
    file.close() #closing the file

def return_update_file(return_, return_quan):
    """
    this function also updates the equipments.txt file
    this function overwrites the details of the equipments
    it increases the quantity of the equipment which is returned by how many items are returned
    """
    qq = read_equipments() #calling the function in qq
    total_quantity_ = qq[return_][3] #getting quantity value from dictionary
    updated_quantity_ = int(total_quantity_) + int(return_quan) #calculating value of updated_quantity_
    qq[return_][3] = updated_quantity_ #storing the value in dictionary

    #opening a file to rewrite it
    file = open("equipments.txt","w")

    #using for loop to update the value of quantity
    for value in qq.values():
        file.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]))
        file.write("\n")
    file.close() #closing the file
