def Entery():
    print("------------------------------")
    city= input("Enter the city name: ")
    date= input("Date (DD-MM-YYYY): ")
    temp= input("Temperature: ")
    hum= input("Humidity: ")
    con= input("Weather condition (e.g. Sunny, Rainy): ")

    dic1= {"date": date, "temp": temp ,"hum": hum ,"con": con}
    dic2={city.upper():[dic1]}
    print(f"The data for {city.upper()} has been entered!")
    return dic2

def Search(dic):
    print("------------------------------")
    city= input("Enter the city name: ")
    for key in dic.keys():
        if city.upper() == key:
            for value in dic[key]:
                print("------------------------------")
                print(f"\nInformation for {city.upper()}\nDate: {value['date']} \nTemperature: {value['temp']}\nHumidity: {value['hum']} \nWeather condition: {value['con']}")
        else:
            print(f"Sorry, we don't have data for {city.upper()}\nTry to enter it by youself :)")

def Update(dic):
    print("------------------------------")
    city = input("Enter the city name: ")
    if city.upper() in dic:
        date = input("Enter the date to update (DD-MM-YYYY): ")
        for value in dic[city.upper()]:
            if value["date"] == date:
                temp = input("Enter new Temperature: ")
                hum = input("Enter new Humidity: ")
                con = input("Enter new Weather condition: ")
                value["temp"] = temp
                value["hum"] = hum
                value["con"] = con
                print("Data has been updated!")
                return dic
        print(f"No data found for date {date} in {city.upper()}")
    else:
        print(f"Sorry, we don't have data for {city.upper()}")
    return dic

def Delete(dic):
    print("------------------------------")
    city = input("Enter the city name: ")
    if city.upper() in dic:
        date = input("Enter the date to delete (DD-MM-YYYY): ")
        for value in dic[city.upper()]:
            if value["date"] == date:
                dic[city.upper()].remove(value)
                if not dic[city.upper()]:
                    del dic[city.upper()]
                print(f"Data for {date} in {city.upper()} has been deleted!")
                return dic
        print(f"No data found for date {date} in {city.upper()}")
    else:
        print(f"Sorry, we don't have data for {city.upper()}")
    return dic

dic =''
choice=0
while True:
    print("\n---------- Welcome ----------\nOur Services\n1. Enter weather data\n2. Search for city\n3. Update \n4. Delete \n5. Exit")
    print("------------------------------")
    choice= eval(input("Enter your choice: "))
    
    if choice == 1:
       dic = Entery()
    elif choice == 2:
      Search(dic)
    elif choice == 3:
      Update(dic)
    elif choice == 4:
      Delete(dic)
    elif choice == 5:
       print("Thank you for using our program, GoodBye :)")
       exit()
    else:
      print("Invalid choice")