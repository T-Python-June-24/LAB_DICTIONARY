# # LAB_DICTIONARY


# ## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
# You can follow the table below:

# | Name    | Number      |
# | -------- | ---------- |
# | Amal     | 0568323222 |
# | Mohammed | 0522222232 |
# | Khadijah | 0532335983 |
# | Abdullah  | 0545341144 |
# | Rawan    | 0545534556 |
# | Faisal   | 0560664566 |
# | Layla    | 0567917077 |


# - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
# - If the number is less or more than 10 numbers, print "This is invalid number".
# - If the number contains letters or symbols, print "This is invalid number".

# ## Q2:Write a function that receives a list containing the following numbers : 
# - [5, 0, 34, 9, 0, 13, 8]
# - rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.



###1

phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

def lookupNum(number):
    if len(number) != 10:
        return "This is an invalid number"
    if not number.isdigit():
        return "This is an invalid number"
    return phone_book.get(number, "Sorry, the number is not found")



phone_number = input("Enter the phone number: ")

print(lookupNum(phone_number))



print(f"\n\n\n", "_"*25, "\n\n\n")

###2

def arranging_list(lst):
    notZero = [x for x in lst if x != 0]
    isZero = [x for x in lst if x == 0]
    return notZero + isZero



list1 = [5, 0, 34, 9, 0, 13, 8]

print(arranging_list(list1))
