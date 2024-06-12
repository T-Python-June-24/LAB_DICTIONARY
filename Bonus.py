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


def Wether_data(weather_dictionary):

   city_name=input("City name : ")
   date=input("Date (YYYY-MM-DD): ")
   temperature=input("Temperature (°C):")
   humidity=input("Humidity (%): ")
   weather_condition=input("weather condition (e.g., sunny, rainy)")
   
   weather_dictionary["city_name":city_name]={"date":date,
                                              "temperature":temperature,
                                              "humidity":humidity,
                                              "weather_condition":weather_condition}
   print(weather_dictionary)
  
weather_dictionary={}
while True:
 user_input=input("to enter weather data press 1 to cheack the weather press 2  to exit press 3 ") 
 if user_input=="1" :
    Wether_data(weather_dictionary)
 
 else :
  print("invalid input")







   