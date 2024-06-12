#Q1
my_dictionary={"Amal": "0568323222",
               "Mohammed": "0522222232",
               "Khadijah":"0532335983",
               "Abdullah":"0545341144",
               "Rawan"	:"0545534556",
               "Faisal":"0560664566",
               "Layla":"0567917077"
}
values=my_dictionary.values()
values_list=list(values)

keys=my_dictionary.keys()
keys_list=list(keys)
def find_owner(my_dictionary):
 values=my_dictionary.values()
 values_list=list(values)

 keys=my_dictionary.keys()
 keys_list=list(keys)   
 user_input=input("Enter the number to provied you with the owner : ")
 if user_input.isdigit():
   if  len(user_input)!=10:
       print("This is invalid number ")
   if values_list.__contains__(user_input):
    for key in keys_list:
        if my_dictionary[key]==user_input:
            print(f"The owner of {user_input} is {key}")
   else:
     print("Sorry, the number is not found")
 else:
   print("This is invalid number")

find_owner(my_dictionary)
