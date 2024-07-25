#defining a function
def read_equipments():
    """
    this function reads the content of the equipmwnts.txt file
    then it accesses its content and puts it in a dictionary and returns its value
    this helps accessing the contents of the equipments file more efficient and simple
    """

    #opening the file 'equipments.txt' to access its content
    file = open("equipments.txt", "r") 

    data = (file.read()) #reading the file
    file.close() #closing the file
    data = data.split("\n") #splitting the content of the file on the bais of new line

    c=1
    d = {} #initializing a dictionary

    #using for loop to put the content in the dictionary
    for i in range(len(data)):
        d[c]=data[i].split(",")
        c = c+1

    return d #returning the value of the dictionary

