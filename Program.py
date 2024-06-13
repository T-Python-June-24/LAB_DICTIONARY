phoneBook = {
    "Amal": "568323222",
    "Mohammed": "522222232",
    "Khadijah": "532335983",
    "Abdullah": "545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

def findOwner (phoneNumber:int) :

    phoneNumber_str = str(phoneNumber)
    if len(phoneNumber_str) != 9:
        print("This is invalid number", phoneNumber_str)
        return
    for name, number in phoneBook.items():
        if number == phoneNumber_str:
            print(f"The owner of the number {phoneNumber_str} is {name}")
            return
    print("Sorry, the number is not found")

try:
    userInput = input("Please Enter a Phone Number: ")
    inputNumber = int(userInput)
    findOwner(inputNumber)
except ValueError:
    print("This is invalid number, You must enter a valid 10-digit phone number")

