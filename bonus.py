'''

# Bonus (use a new file)

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



Each entry should include
1-the city name,
2- date, temperature,
3-humidity,
4-
weather condition (e.g., sunny, rainy).

'''

Weather = { 
           
           
           "riyadh" : { "Date" : "12/12/2024", "Temperature" : "50 C", "Humidity" : "112°F", "Weather Condition" : "Sunny" },
           
           "makkah" : { "Date" : "12/12/2024", "Temperature" : "30 C", "Humidity" : "112°F", "Weather Condition" : "rainy" },
           
           "jeddah": {"Date" : "12/12/2024", "Temperature" : "30 C", "Humidity" : "112°F", "Weather Condition" : "Sunny"},
           
            "Al-bahah": {"Date" : "12/12/2024", "Temperature" : "3 C", "Humidity" : "112°F", "Weather Condition" : "rainy"},
           
           
           
           }

def add_weather_data(city:str, date, temperature:str, humidity:str, weather_condition:str): #!function to add data to dictionary
    Weather[city] = {"Date" : date, "Temperature" : temperature, "Humidity" : humidity, "Weather Condition" : weather_condition}
    for key, value in Weather.items():
        print(f"{key} | {value} ") #!dispaly the data in good way
    return Weather

# add_weather_data(input("Please Enter City Name 🏙️: "), input("Please Enter Date 🗓️: "), input("Please Enter Temperature 🌡️: "), input("Please Enter Humidity 🌡️: "), input("Please Enter Weather Condition 🤔: ") )
#! each input will be stored in the dictionary and the city name must be unique 

def query_by_city(city:str):
    '''
    Arg:  city name
    
    '''
    if city in Weather:
        # print(Weather[city])
        for key, value in Weather[city].items():#!for loop to display the key and value in dictionary and the city name from must match the city name in the dictionary ولا مارح تجيني النتيجة
            print(f"{key} : {value}")#!dispaly the data in good way
    else:
        print("City not found")
        
        
# query_by_city(input("Please Enter City Name : "))



def update_weather_data(city, date, temperature, humidity, weather_condition):
    '''
    
    Arg: city name, date, temperature, humidity, weather condition
    
    '''
    if city in Weather:
        Weather[city] = {"Date" : date, "Temperature" : temperature, "Humidity" : humidity, "Weather Condition" : weather_condition}
        print(Weather[city])
        return Weather
    else:
        print("City not found")
        
# update_weather_data(input("Please Enter City Name : "), input("Please Enter Date : "), input("Please Enter Temperature : "), input("Please Enter Humidity : "), input("Please Enter Weather Condition : ") )   


def delete_weather_data(city):
    '''
    Arg: city name "key"
    '''
    if city in Weather:
        del Weather[city]
        return Weather
    else:
        print("City not found")
        
# delete_weather_data(input("Please Enter City Name : "))    



def display_weather_data():
    ''' 
     
      Display all weather data in the dictionary
      
       ''' 
    for key, value in Weather.items():
        print(f"{key} | {value} ")
        
# display_weather_data()


print("\n\n"+"<------------------welcome to weather data aggregation------------------>")
def menu():
    while True:
        print("\nWelcome to Weather Data Aggregation 👋")
        print("1. Add weather data🌤️")
        print("2. Query by city🏙️")
        print("3. Update weather data📊")
        print("4. Delete weather date🗑️")
        print("5. Display all weather data🌎")
        print("6. Exit 🚪")

        choice = input("Please enter your choice: ")

        if choice == '1':
            city = input("Enter city name: ")
            date = input("Enter date: ")
            temperature = input("Enter temperature: ")
            humidity = input("Enter humidity: ")
            weather_condition = input("Enter weather condition: ")
            add_weather_data(city, date, temperature, humidity, weather_condition)
        elif choice == '2':
            city = input("Enter city name: ")
            query_by_city(city)
        elif choice == '3':
            city = input("Enter city name: ")
            date = input("Enter date: ")
            temperature = input("Enter temperature: ")
            humidity = input("Enter humidity: ")
            weather_condition = input("Enter weather condition: ")
            update_weather_data(city, date, temperature, humidity, weather_condition)
        elif choice == '4':
            city = input("Enter city name: ")
            delete_weather_data(city)
        elif choice == '5':
            display_weather_data()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
menu()