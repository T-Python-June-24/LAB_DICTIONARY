# initialized a dictionary to store the weather data
weather_aggregate = {}


def add_city() -> None:
    """
    This function allows the user to add weather data for a specific city.
    
    args:
        None
        
    returns:
        None
    """
    city = input("Enter the city name: ")
    while not city.strip():
        city = input("You entered an invalid city name, please enter a valid city name: ")

    temperature = input("Enter the temperature: ")
    while not temperature.isdigit():
        temperature = input("You entered an invalid temperature, please enter a valid temperature: ")

    date = input("Enter the date in this format (dd-mm-yyyy): ")
    while not (len(date) == 10 and date[2] == "-" and date[5] == "-" and 
               date[:2].isdigit() and date[3:5].isdigit() and date[6:10].isdigit() and 
               1 <= int(date[:2]) <= 31 and 1 <= int(date[3:5]) <= 12 and 
               2000 <= int(date[6:10]) <= 2024):
        date = input("You entered an invalid date, please enter a valid date in this format (dd-mm-yyyy): ")

    humidity = input("Enter the humidity: ")
    while not humidity.isdigit():
        humidity = input("You entered an invalid humidity, please enter a valid humidity: ")

    weather_condition = input("Enter the weather condition (only choose from these options, Sunny, Rainy, Snowy, Cloudy): ").capitalize()
    while weather_condition not in ["Sunny", "Rainy", "Snowy", "Cloudy"]:
        weather_condition = input("You entered an invalid weather condition, please enter a valid weather condition (only choose from these options, Sunny, Rainy, Snowy, Cloudy): ").capitalize()

    if city not in weather_aggregate:
        weather_aggregate[city] = {}
    weather_aggregate[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "weather_condition": weather_condition
    }
    print("Data added successfully.")
    print(weather_aggregate[city])


def search_for_cities() -> None:
    """
    This function allows the user to search for weather data for a specific city and date.
    
    args:
        None
        
    returns:
        None
    """
    print("Available cities: ", list(weather_aggregate.keys()))
    city = input("Enter the city name: ")
    date = input("Enter the date in this format (dd-mm-yyyy): ")
        
    if city in weather_aggregate and date in weather_aggregate[city]:
        print("City: ", city)
        print("Date: ", date)
        print("Temperature: ", weather_aggregate[city][date]["temperature"])
        print("Humidity: ", weather_aggregate[city][date]["humidity"])
        print("Weather Condition: ", weather_aggregate[city][date]["weather_condition"])
    else:
        print("Sorry, no data found for this city or date.")
        print("Available data for cities: ", list(weather_aggregate.keys()))

def delete_city():
    city = input("Enter the city name: ")
    date = input("Enter the date in this format (dd-mm-yyyy): ")
    if city in weather_aggregate and date in weather_aggregate[city]:
        del weather_aggregate[city][date]
        print("City deleted successfully.")
    else:
        print("City not found.")

def update_city():
    """
    This function allows the user to update weather data for a specific city and date.
    
    args:
        None
        
    returns:
        None
    """
    city = input("Enter the city name: ")
    date = input("Enter the date in this format (dd-mm-yyyy): ")
    if city in weather_aggregate and date in weather_aggregate[city]:
        temperature = input("Enter the new temperature: ")
        while not temperature.isdigit():
            temperature = input("You entered an invalid temperature, please enter a valid temperature: ")
        humidity = input("Enter the new humidity: ")
        while not humidity.isdigit():
            humidity = input("You entered an invalid humidity, please enter a valid humidity: ")
        weather_condition = input("Enter the new weather condition (only choose from these options, Sunny, Rainy, Snowy, Cloudy): ").capitalize()
        weather_aggregate[city][date] = {
            "temperature": temperature,
            "humidity": humidity,
            "weather_condition": weather_condition
        }
        print("City updated successfully.")
    else:
        print("City not found.")

while True:
    menu = (
        "Please select an option from the menu:\n"
        "1: Add weather data\n"
        "2: Search weather data\n"
        "3: Delete weather data\n"
        "4: Update weather data\n"
        "5: Exit\n"
        "Enter your choice (1-5): "
    )  
    user_choice = input(menu)
    if user_choice == "1":
       add_city()
       
    elif user_choice == "2":
       search_for_cities()
       
    elif user_choice == "3":
       delete_city()
       
    elif user_choice == "4":
       update_city()
    
    elif user_choice == "5":
        break
    
    else:
        print("Invalid choice, please enter 1, 2, 3, 4, or 5.")

print("Thanks for using our weather app")
