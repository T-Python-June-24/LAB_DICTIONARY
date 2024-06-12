import re

# - Validate user inputs to ensure correctness.
def is_alphabetic(string:str) -> bool:
    '''
    Checks if a string is alphbetic.
    
    Args:
        string (str): A name of a city.

    Returns: True if the string as alphabetic.
             False otherwise.
    '''
    check:list = string.split()
    for name in check:
        if name.isalpha():
            continue
        else:
            return False
    return True

# - Validate user inputs to ensure correctness.
def is_date(date:str) -> bool:
    '''
    Checks if a string follows this pattern: DD(-|_|.|/)MM(-|_|.|/)YYYY.
    
    Args:
        string (str): A name of a city.

    Returns: True if the string follows this pattern: DD(-|_|.|/)MM(-|_|.|/)YYYY.
             False otherwise.
    '''
    pattern:str = "(0?[1-9]|[12][0-9]|3[01])(-|_|\.|\/)(0?[1-9]|1[12])(-|_|\.|\/)(1?9?|2?0?)[\d]{2}"
    if re.search(pattern, date):
        return True
    else:
        return False

# 1. **Input Weather Data:** Allow the user to input weather data for different cities.
# Each entry should include the city name, date, temperature, humidity, and
# weather condition (e.g., sunny, rainy).

# 2. **Store Data in a Dictionary:** Use a nested dictionary to store the weather data.
# The outer dictionary's keys will be the city names, and the values will be another
# dictionary containing date and weather details.

# - Implement separate functions for inputting data, querying by city.
def input_log(weather_record:dict):
    '''
    Creates an entry in a dictionary provided that the values are validated.

    Args:
        weather_record (dict): A dictionary of weather data.

    Returns:
        None
    '''    
    print("\n___Logging System___\n")
    city:str = input("City: ")
    if is_alphabetic(city):
        date:str = input("Date: ")
        if is_date(date):
            temp:str = input("Teperature: ")
            if temp.isdigit():
                temp += " °C"
                humid:str = input("Humidity: ")
                if humid.isdigit() and int(humid) >= 0 and int(humid) <= 100:
                    humid += "%"
                    weather:str = input("Weather condition: ")
                    if is_alphabetic(weather):
                        weather_record[city] = {"Date": date, "Temperature": temp, "Humidity": humid, "Weather condition": weather}
                        print(f"\nEntry {city} was logged successfully!\n")
                        return
                    else:
                        print("The weather must be in alphabetic characters!")
                        return
                else:
                    print("The humidity must be a number between 0 and 100!")
                    return
            else:
                print("The temperature must be in digits!")
                return
        else:
            print("The date follow this pattern: DD(-|_|.|/)MM(-|_|.|/)YYYY! and be between 01/01/1900 and 31/12/2099")
            return
    else:
        print("The city must contain only alphabetic characters!")
        return

# 3. **Query by City:** Allow the user to query the weather data by city name,
# displaying all the recorded weather data for that city.
# - Implement separate functions for inputting data, querying by city.
def query_system(weather_record:dict):
    '''
    Displays the values of an entry in a dictionary.

    Args:
        weather_record (dict): A dictionary of weather data.

    Returns:
        None
    '''    
    while True:
        print("\n___Querying System___\n")
        choice:str = input("Enter the city name or 0 to go back to the main menu: ")
        if choice.isdigit():
            if int(choice) == 0:
                return
            else:
                print("Invalid input.")
        else:
            print(weather_record.get(choice, "This city is not in our records. Try another city."))

# Challenge:
# - Extend the program to allow the user to update or delete weather data for a specific city and date.
def update_system(weather_record:dict):
    '''
    Updates or deleted an entry in a dictionary.

    Args:
        weather_record (dict): A dictionary of weather data.

    Returns:
        None
    '''
    while True:
        print("\n___Update_System___\n")
        choice:str = input("Enter 1 to update an entry, 2 to delete an entry, or 0 to go back to the main menu: ")
        if choice.isdigit():
            if int(choice) == 0:
                return
            elif int(choice) == 1:
                input_log(weather_record)
            elif int(choice) == 2:
                if choice in weather_record:
                    del weather_record[choice]
                    print("Deleted successfuly.")
                else:
                    print("This city is not in our records. Try another city.")
            else:
                print("Invalid entry.")

print("Welcome to the weather logging system!")
weather_record:dict = {}

while True:
    choice:str = input("Please enter 1 to input data, 2 to query the system, 3 to update the system, or 0 to exit: ")
    if choice.isdigit():
            if int(choice) == 0:
                break
            elif int(choice) == 1:
                input_log(weather_record)
            elif int(choice) == 2:
                query_system(weather_record)
            elif int(choice) == 3:
                update_system(weather_record)
            else:
                print("Invalid input.")
    else:
        print("Please enter a number...")

print("Thank you for using the weather logging system!")


