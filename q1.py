'''

# LAB_DICTIONARY


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah  | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".

'''

phone_book = {  
              
            "0568323222": "Amal",
            "0522222232": "Mohammed",
            "0532335983": "Khadijah",
            "0545341144": "Abdullah",
            "0545534556": "Rawan",
            "0560664566": "Faisal",
            "0567917077": "Layla",
            }

number = input("Please Enter Postive Number :  ")


if len(number) != 10:
    print("This is invalid number...")
elif  not number.isdigit():
    print("please enter a valid number") 
elif number in phone_book:
    print(f"This Number Bleongs to : {phone_book[number]} ")
    
else:
    print("Sorry, the number is not found")


'''

## Q2:Write a function that receives a list containing the following numbers : 
- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.


'''

# def arrange_list(lst):
#     non_zeros = [i for i in lst if i != 0]
#     zeros = [0] * lst.count(0)
#     return non_zeros + zeros

# print(arrange_list([5, 0, 34, 9, 0, 13, 8]))


#!the second way to solve the problem
def arrange_list2(lst):
    lst.sort(key=lambda x: x == 0)
    return lst

print(arrange_list2([5, 0, 30, 9, 0, 13, 8]))













