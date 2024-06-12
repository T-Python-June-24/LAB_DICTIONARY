contacts = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

# create a reversed version of the dictionary
reversed_contacts = {number: name for name, number in contacts.items()}

contact_number = input("Enter the number you want to look for: ")

# validation for the number
is_valid = len(contact_number) == 10 and contact_number.isdigit()
# searching for a number
is_found = contact_number in reversed_contacts

if not is_valid: 
    print("This is Invalid number")
    exit()
elif not is_found:
    print("Sorry, this number is not found")
else:
    print(f"{reversed_contacts[contact_number]} has the number {contact_number}")
