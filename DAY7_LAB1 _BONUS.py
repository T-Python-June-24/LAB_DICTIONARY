# # Bonus (use a new file)

# ### Exercise: Weather Data Aggregation

# **Objective:** Write a Python program that aggregates weather data for different cities and provides weather data based on user queries.

# #### Requirements:

# 1. **Input Weather Data:** Allow the user to input weather data for different cities. Each entry should include the city name, date, temperature, humidity, and weather condition (e.g., sunny, rainy).
# 2. **Store Data in a Dictionary:** Use a nested dictionary to store the weather data. The outer dictionary's keys will be the city names, and the values will be another dictionary containing date and weather details.
# 3. **Query by City:** Allow the user to query the weather data by city name, displaying all the recorded weather data for that city.

# #### Guidelines:

# - Use nested dictionaries to store the weather data efficiently.
# - Implement separate functions for inputting data, querying by city.
# - Validate user inputs to ensure correctness.

# #### Challenge:

# - Extend the program to allow the user to update or delete weather data for a specific city and date.



def input_weather_data():

    weather_data = {}

    while True:
        city = input("Enter city name (or type 'exit' to stop): ").strip()
        if city.upper() == 'EXIT':
            break


        date = input("Enter date (YYYY-MM-DD): ").strip()
        temperature = input("Enter temperature (in Celsius): ").strip()
        humidity = input("Enter humidity (in percentage): ").strip()
        condition = input("Enter weather condition (e.g., sunny, rainy): ").strip()


        
        try:
            temperature = float(temperature)
            humidity = int(humidity)

        except ValueError:
            print("Invalid temperature or humidity. Please enter numeric values")
            continue

        # Store
        if city not in weather_data:
            weather_data[city] = {}
        
        weather_data[city][date] = {
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
        }

        print("Weather data added successfully")

    return weather_data





def query_by_city(weather_data):

    while True:
        city = input("Enter city name to query (or type 'exit' to stop): ").strip()
        # city = input("Enter city name to query (or type 'exit' to stop OR 'new' to add city): ").strip()

        if city.upper() == 'EXIT':
            break
        # elif city.upper() == 'New':
        #     weather_data = input_weather_data(weather_data)
        #     continue


        if city in weather_data:
            print(f"Weather data for {city}:")
            for date, data in weather_data[city].items():
                print(f"\tDate:\t\t {date}")
                print(f"\tTemperature:\t {data['temperature']} °C")
                print(f"\tHumidity:\t {data['humidity']}%")
                print(f"\tCondition:\t {data['condition']}")
        else:
            print(f"No weather data found for city: {city}")







def main():
    weather_data = input_weather_data()
    query_by_city(weather_data)



main()