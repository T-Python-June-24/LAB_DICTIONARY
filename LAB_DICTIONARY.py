# Question 1

def phonesBook(phoneNumber:str)->None:
    '''
    this function takes an number and return the name of the onwer of that naumber.

    Args:
    phoneNumber:str
    return: 
    None
    '''
    
    names=['Amal','Mohammed',
    'Khadijah',
    'Abdullah',
    'Rawan',
    'Faisal',
    'Layla',]
    phones=['0568323222',
    '0522222232',
    '0532335983',
     '0545341144',
    '0545534556',
    '0560664566',
    '0567917077',]
    phoneOwners={phone:name for phone ,name in zip(phones,names) }
    if (phoneNumber.isdigit()):
        if(len(phoneNumber)==10):
            if(phoneNumber in phoneOwners):
                print(f"The owner is {phoneOwners[phoneNumber]}")
            else:
                print(f"There is no onwer for this number {phoneNumber}")
        else:
            print("Invalid phone number it should be 10 digit")
    else:
        print("This is invalid number, please try to enter a real number")
phonesBook(input("Please enter a phone number: "))


# Question 2:

def arrangeList(Numbers:list)->list:
    return  sorted(Numbers,reverse=True)

Numbers=[5, 0, 34, 9, 0, 13, 8]
print(arrangeList(Numbers))

