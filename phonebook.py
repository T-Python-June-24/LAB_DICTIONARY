
phonebook = {"0568323222" : "Amal",
            "0522222232" : "Mohammed",
            "0532335983" : "Khadijah",
            "0545341144" : "Abdullah",
            "0545534556" : "Rawan",
            "0560664566" : "Faisal",
            "0567917077" : "Layla" }

input:str = input("Please enter your number: ")

if len(input) != 10 or not input.isdigit():
    print("This is an invalid number")
else:
    found = False
    for(number, name) in phonebook.items():
        if number == input:
            found = True
            print("Owner: ", name)
    if not found:
        print("Sorry, the number is not found!")


