# take phone number input from the user
phone_number = input("Enter the phone number: ")

# Defining the dictionary
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

# Function to get the owner by phone number
def get_owner(phone_number):
    # Check if the phone number is exactly 10 digits and contains only numbers
    if len(phone_number) != 10 or not phone_number.isdigit():
        return "This is invalid number"
    
    # check if the phone number exicit in the dictionary
    owner = phone_book.get(phone_number)
    
    # Return the owner's name if found, otherwise an error message
    if owner:
        return owner
    else:
        return "Sorry, the number is not found"


# calling the function and printing the result
print(get_owner(phone_number))



# Define the list
numbers_list = [5, 0, 34, 9, 0, 13, 8]

# defining the function to rearrange the list
def rearrange_list(numbers:list):
    # Separate zero numbers
    list_numbers = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]
    
    # Concatenate zeros with numbers in the list
    rearranged_list = list_numbers + zeros
    
    return rearranged_list


rearranged_list = rearrange_list(numbers_list)
print(rearranged_list)
