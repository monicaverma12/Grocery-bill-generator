#print the name of any supermarket
print ("                     ----- Carrefour -----            ")

#print the headings for the bill
print("\n\nProduct       quantity    Price/unit($)         Total price")

#create a list of items with their unit price
products = {

  "milk":2.0,
  "coffee":3.0,
  "tea":2.5,
  "nuts":5.0,
  "cookies":4.0,
  "bread":4.5
  }

#define a variable for grand total
total = 0


def pro():

  #globalize the variable for its usabilty
  global total 

  #take list of items from user and convert to lower-case
  user = input("\n")
  user = user.lower()

  if user in products:

    #take quantity of items from the user
    quantity = int(input("\t\t\t\t"))

    #update contents in the table
    print ("\t\t\t\t\t\t\t\t", products[user],"\t\t\t\t", quantity*products[user])

    #calculate the grand total
    total = total + (quantity*products[user])
  
  elif user =="end":
    #check final item as end to find grand total
    print("----------------------------------------------------------")
    print("                Grand Total                         ", total)



#call the function
while True:
  pro()

"""Product       quantity    Price/unit($)         Total price 

coffee

                 2 
                                              
                              3                      6
Tea  



---------------------------------------------------------------
 Grand Total -                              55$"""



