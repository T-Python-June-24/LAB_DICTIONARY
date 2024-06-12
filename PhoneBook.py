NameNo = {
    '0568323222' : "Amal",
    '0522222232' : "Mohammed",
    '0532335983' : "Khadijah",
    '0545341144' : "Abdullah",
    '0545534556' : "Rawan",
    '0560664566' : "Faisal",
    '0567917077' : "Layla" 
    }

PhoneNo = input("Enter a phone No: ")

if PhoneNo in NameNo:
    print(f"The Phone number {PhoneNo} belongs to {NameNo[PhoneNo]}")

elif len(PhoneNo) != 10:
    print("This is an invalid Number")

elif PhoneNo.isdigit() == False:
    print("Phone Numbers contain digits only")

else:
    print("Sorry, The phone Number hasn't been found")