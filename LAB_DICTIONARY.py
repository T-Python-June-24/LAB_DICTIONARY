#Q1
my_dictionary={"Amal": "0568323222",
               "Mohammed": "0522222232",
               "Khadijah":"0532335983",
               "Abdullah":"0545341144",
               "Rawan"	:"0545534556",
               "Faisal":"0560664566",
               "Layla":"0567917077"
}

def find_owner(my_dictionary):
 '''
 this function findes the owner for a number was given by the user
 Args:
 my_dictionary(dictionary): contains the owners and thier numbers
 '''
 #creat a list contains the values (Numbers in the dictionary)
 values=my_dictionary.values()
 values_list=list(values)
 
 #creat a list contains the keys (owners in the dictionary)
 keys=my_dictionary.keys()
 keys_list=list(keys)  
 #take the number input from a user  
 user_input=input("Enter the number to provied you with the owner : ")
 if user_input.isdigit(): # check if its contains letters or symbols
   if  len(user_input)!=10:
       print("This is invalid number ")
   if values_list.__contains__(user_input): # if the user input exist in the dicitonary 
    for key in keys_list:
        if my_dictionary[key]==user_input: # find the key of the value (number fron the user)
            print(f"The owner of {user_input} is {key}")
   else:
     print("Sorry, the number is not found")
 else:
   print("This is invalid number")

find_owner(my_dictionary)


my_list=[5, 0, 34, 9, 0, 13, 8]

def list_sorting(my_list):
   '''
   this function rearranges the list so the zeros at the end of the list
   Args:
   my_list(list): list with integer items 
   Returns:
   my_sorte_list(list): all the zeros in the list are at the end 
   '''
   non_zero_list=[i for i in my_list if i!=0]
   zero_list=[i for i in my_list if i==0]
   my_sorte_list=non_zero_list+zero_list
   return my_sorte_list
my_sorte_list=list_sorting(my_list)
print(my_sorte_list)