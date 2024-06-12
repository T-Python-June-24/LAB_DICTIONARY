
phoneBook = {
            "Amal" : "0568323222",
             "Mohammed" : "0522222232",
             "Khadijah" : "0532335983",
             "Abdullah" : "0545341144",
             "Rawan" : "0545534556",
             "Faisal" : "0560664566",
             "Layla" : "0567917077"
             }

number = input("Enter the phone number: ")
if len(number) == 10 and number.isdigit():
    found = False
    for key, value in phoneBook.items():
        if value == number:
            print(f"The phone number {value} belongs to {key}")
            found = True
            break
    if found == False:
        print("Sorry, the owner is not found!")
else:
    print("This is invalid number!")

