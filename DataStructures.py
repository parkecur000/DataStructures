#Curtis Parker
#Data Structure Assignment
"""Description:
    Goal: Track exactly how many hamburgers each customer eats
    Create a new Python application that implements various data structures. 
        •	Create a variable for a Queue with items of type string o This variable will represent your line of customers waiting outside. 
        •	Create a variable for a Dictionary with keys of type string and values of type int. 
            o This variable will hold information about each customer 
        •	Put 100 customers into the queue o You can use the random class to generate random people for your line 
        •	Add a random number of burgers to the total for each customer. Make sure there is a key in the dictionary for each customer before you try incrementing their total! 
        •	Print out each customer and their total burgers eaten. 
    NOTE: Remember that a queue in Python is a list data structure. 

Here is some code that will help you with this project.  
def randomName() :
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    iRandomNum = random.randint(0,8)
    return asCustomers[iRandomNum]

def randomBurgers() :
    return random.randint(1, 20)

"""
import random as random
import collections as collections

#generate a random customer name from the list of names given
def randomName() :
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    iRandomNum = random.randint(0,8)
    return asCustomers[iRandomNum]

#generate a random number between 1 and 20 for number of burgers
def randomBurgers() :
    return random.randint(1, 20)

#Initiate the queue for customers and a dictionary
queue = []
dictCustomers = {}

#Place 100 customers in the queue
for i in range(0,100) :
    queue.append(randomName())

#go through each customer and "take their order" for number of burgers. Put their information in a dictionary
while (len(queue) > 0) :
    sCustomer = str(queue[0])
    if sCustomer not in dictCustomers :
        dictCustomers[sCustomer] = 0
        dictCustomers[sCustomer] += randomBurgers()
    else :
        dictCustomers[sCustomer] += randomBurgers()
    queue.pop(0)

#Sort through the customers in descending order for most eaten burgers
listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True)

#Print the customer name out with the obsured number of burgers they have ordered
for customer in listSortedCustomers :
    print(customer[0].ljust(19), customer[1])
