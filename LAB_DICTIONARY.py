# Q1:Build a phone book program that receives the phone number
# (Use Input to let the user provide the number), and returns
# the name of the owner. 
# You can follow the table below:
# | Name     | Number     |
# | -------- | ---------- |
# | Amal     | 0568323222 |
# | Mohammed | 0522222232 |
# | Khadijah | 0532335983 |
# | Abdullah | 0545341144 |
# | Rawan    | 0545534556 |
# | Faisal   | 0560664566 |
# | Layla    | 0567917077 |
# - If the number exists, print the owner. Otherwise, print
# "Sorry, the number is not found".
# - If the number is less or more than 10 numbers, print
# "This is invalid number".
# - If the number contains letters or symbols, print
# "This is invalid number".

phone_book:dict = {"0568323222": "Amal", "0522222232": "Mohammed", "0532335983": "Khadijah",
                   "0545341144": "Abdullah", "0545534556": "Rawan", "0560664566": "Faisal",
                   "0567917077": "Layla"}
number:str = input("Provide the number: ")
if len(number) == 10 and number.isdigit():
    print(phone_book.get(number, "Sorry, the number is not found"))
else:
    print("This is invalid number")

# Q2:Write a function that receives a list containing the following numbers : 
# - [5, 0, 34, 9, 0, 13, 8]
# - rearranges the list so that the zeros are the end of the list,
# and finally returns the arranged list.

num_list:list = [5, 0, 34, 9, 0, 13, 8]

def zero_appender(numbers:list) -> list:
    '''
    Takes a list and returns a new list withh zeroes at the end "if any"
    
    Args:
        numbers (list): a list of numbers.

    Returns:
        new_list (list): a list of numbers with zeroes at the end.
    '''
    # Copy the content of the passed list
    new_list = numbers.copy()
    for index in range(len(new_list)):
        # If the current number is a zero append it to the end of the list
        if new_list[index] == 0:
            new_list.append(new_list.pop(index))
        
    return new_list

print(zero_appender(num_list))





