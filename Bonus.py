
def Entery(dic):
    print("------------------------------")
    city= input("Enter the city name: ")
    date= input("Date: ")
    temp= input("Temperature: ")
    hum= input("Humidity: ")
    con= input("Weather condition (e.g. Sunny, Rainy): ")

    dic1= {"date": date, "temp": temp ,"hum": hum ,"con": con}

    if city.upper() in dic:
       dic[city.upper()].append(dic1)
    else:
        dic[city.upper()]= [dic1]

    print(f"The data for {city} has been entered!")
    return dic

def Search(dic):
    print("------------------------------")
    city= input("Enter the city name: ")
    for key in dic.keys():
        if city.upper() == key:
            for value in dic[city]:
                print(f"\nInformation for {city.upper()}\nDate: {value['date']} \nTemperature: {value['temp']}\nHumidity: {value['hum']} \nWeather condition: {value['con']}")
        else:
            print(f"Sorry, we don't have data for {city}\nTry to enter it by youself :)")

dic =''
choice=0
while True:
    print("\n---------- Welcome ----------\nOur Services\n1. Enter weather data\n2. Search for city\n3. Exit")
    print("------------------------------")
    choice= eval(input("Enter your choice: "))
    
    if choice == 1:
       dic = Entery()
    elif choice == 2:
      Search(dic)
    elif choice == 3:
       print("Thank you for using our program, GoodBye :)")
       exit()
    else:
      print("Invalid choice")