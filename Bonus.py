'''
### Exercise: Weather Data Aggregation

**Objective:** Write a Python program that aggregates weather data for different cities and provides weather data based on user queries.

#### Requirements:

1. **Input Weather Data:** Allow the user to input weather data for different cities. Each entry should include the city name, date, temperature, humidity, and weather condition (e.g., sunny, rainy).
2. **Store Data in a Dictionary:** Use a nested dictionary to store the weather data. The outer dictionary's keys will be the city names, and the values will be another dictionary containing date and weather details.
3. **Query by City:** Allow the user to query the weather data by city name, displaying all the recorded weather data for that city.

#### Guidelines:

- Use nested dictionaries to store the weather data efficiently.
- Implement separate functions for inputting data, querying by city.
- Validate user inputs to ensure correctness.

#### Challenge:

- Extend the program to allow the user to update or delete weather data for a specific city and date.


Enter weather data ("to enter weather data press 1 to cheack the weather press 2  to exit press 3 "):
City name: Ryiadh 
Date (YYYY-MM-DD): 2024-06-12
Temperature (°C): 31
Humidity (%): 10
Weather condition: Sunny

'''
 


def weather_data(weather_dictionary):
    """
    Allows the user to add new weather data to the weather dictionary.

    Args:
        weather_dictionary (dict): The dictionary containing the weather data.

    """
    print("\n=== Add New Weather Data ===")
    print("Welcome to the Weather Data System. To add a new city's weather, please enter the following information:")

    city_name = input("City name: ")
    date = input("Date (YYYY-MM-DD): ")
    temperature = input("Temperature (°C): ")
    humidity = input("Humidity (%): ")
    weather_condition = input("Weather condition (e.g., sunny, rainy): ")

    weather_dictionary[city_name] = {
        "date": date,
        "temperature": temperature,
        "humidity": humidity,
        "weather_condition": weather_condition
    }

    print(f"\n{city_name} added successfully to the weather dictionary.")
    return weather_dictionary
def query_by_city(weather_dictionary):
    """
    Allows the user to check the weather data for a specific city.

    Args:
        weather_dictionary (dict): The dictionary containing the weather data.

    
    """
    print("\n=== Check Weather ===")
    city = input("Enter the city to check the weather for: ")
    if city in weather_dictionary:
        print(f"\nWeather data for the city of {city}:")
        print(f"Date: {weather_dictionary[city]['date']}")
        print(f"Temperature: {weather_dictionary[city]['temperature']}°C")
        print(f"Humidity: {weather_dictionary[city]['humidity']}%")
        print(f"Weather condition: {weather_dictionary[city]['weather_condition']}")
    else:
     print(f"\nSorry, the city '{city}' is not in the weather dictionary.")
    
def main():
    """
     Handles the user interactions and calls the appropriate functions.

    
    """
    print("\n=== Welcome to the Weather Data System! ===")
    weather_dictionary = {}
    while True:
        user_input = input("\nTo enter weather data, press 1. To check the weather, press 2. To exit, press 3: ")
        if user_input == "1":
            weather_dictionary = weather_data(weather_dictionary)
        elif user_input == "2":
            weather_dictionary = query_by_city(weather_dictionary)
        elif user_input == "3":
            print("\nExiting...")
            break
        else:
            print("\nInvalid input. Please try again.")
main()