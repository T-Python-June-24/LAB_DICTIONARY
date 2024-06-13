# Q1 Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.
'''
If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".

'''

def phone_book(phone_number:str)->str:
        
    phone_dict = {
        "0568323222":"Amal",
        "0522222232":"Mohammed",
        "0532335983":"Khadijah",
        "0545341144":"Abdullah",
        "0545534556":"Rawan",
        "0560664566":"Faisal",
        "0567917077":"Layla",
    }


    if not phone_number.isnumeric() or (len(phone_number) < 10 or len(phone_number) > 10):

        return phone_dict.get(phone_number,"\n this is invalid number \n ")
        
        
    # elif len(phone_number) < 10 or len(phone_number) > 10 :

    #     print("\n This is invalid number is less than or more than 10 ")

    elif phone_number in phone_dict :

        print(f"\n The owner of number {phone_number} is", end=" ")

        return phone_dict.get(phone_number)
    
    else :

        return "\n This number is not in our numbers book \n "

        # return f"\n The owner of number {phone_number} is " + phone_dict[phone_number]


user_input = (input("\n Enter a number to find who is the owner : "))

print(phone_book(user_input),"\n")
