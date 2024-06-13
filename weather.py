import sys

weatherData= {}
def setCityDetails(city):
    date = input(f"Enter date: ")
    temperature = input(f"Enter temperature: ")
    humidity = input(f"Enter humidity: ")
    weatherCondition = input(f"Enter weather condition: ")
    weatherDetails= {"Date" : date,
    "Tmperature" : temperature,
    "Humidity" : humidity,
    "Weather condition" : weatherCondition}
    return weatherDetails  


def getWeather(city,weatherData = weatherData):
    if city in weatherData:
        print("="*32)
        print(f"CITY: {city}") 
        print("="*32) 
        for key,value in weatherData[city].items():
                print(f"{key}: {value}")
        print("="*32)
    else:
        print(f"{city}'s weather status is not yet available")

def updateWeather(updateOption,weatherData = weatherData,):
    if updateOption == "c":
        city =input("Enter city name: ")
        if city in weatherData:
            weatherDetails = setCityDetails(city)
            weatherData[city] = weatherDetails
            print("="*32)
            print(f"{city}'s weather status has been updated.")

    elif updateOption == "d":
         print("///////Date////////")
         date = input(f"Enter date: ")
         for key,value in weatherData.items():
                #for key in value[date]:
                if value[date] == date:
                    print("DATE FOUND")
                #print(f"{key}: {value}")
    #return weatherDetails

print("Enter city and its weather details: ")
city =input("Enter city name: ")
weatherDetails = setCityDetails(city)
weatherData[city] = weatherDetails

while True:
    print("="*32, "\nPlease press button to proceed: \nA: to add a city. \nV: to view a city weather. \nD: to delete a city. \nU: to update a city weather. \nQ: to quit.")
    print("="*32)
    entry = input()
    print("="*32)
    if entry.lower() == "a":
        city =input("Enter city name: ")
        weatherDetails = setCityDetails(city)
        weatherData[city] = weatherDetails
    elif entry.lower() == "v":
        city = input("Enter a city to view its weather status: ")
        #Getting a city weather data.
        getWeather(city)
    elif entry.lower() == "u":
         updateOption = input("Enter C to update weather by city name or D to update by date: ")
         #weatherData[city] =
         updateWeather(updateOption)
    elif entry.lower() == "q":
        sys.exit()
    else:
        print("Wrong input!")