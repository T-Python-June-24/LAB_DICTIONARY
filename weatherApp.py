


weatherDict:dict={}
def storeWeathreData(cityName:str,temperature:str,humidity:str,weatherCondition:str,date:str)-> dict:

    weatherDict[cityName]={'temperature':temperature,'humidity':humidity,'weatherCondition':weatherCondition,'date':date}



    

def userInterface():
    while True:
        operation=input("Welcom to our weather program see the mune below to be able to use our program \nchoose a number \n1:inserting data\n2:doing query such delete and update\n3:display certain city data\n4:exite the program\n: ")
        if operation.isdigit():
            if int(operation) ==1:
                insertWeatherData()
            elif int(operation)==2:
                queryCity()
            elif int(operation)==3:
                displayCityInfo()
            elif int(operation)==4:
                break
            else:
                print("please enter a number from the mune")
        else:
            print("we only accept numbers. choose from the mune.")




def insertWeatherData():
    try:
        numberOfCities:int=int(input("Please Enter number of cities you want to insert thire weather data: "))
        for i in range(numberOfCities):
            cityName:str=input("Please Enter city name: ")
            temperature:str=input("Please Enter Temperature in Celisus: ")
            humidity:str=input("Please Enter humidity (eg. high mid low): ")
            weatherCondition:str=input("Please Enter weather condition: ")
            date:str=input("please Enter the data (eg. 2024/5/5) : ")
            storeWeathreData(cityName,temperature,humidity,weatherCondition,date)
    except:
        print("something went wrong check your data before entring them.")



def displayCityInfo():
    cityName=input("Please enter city name to display the weather: ")
    if cityName in weatherDict:
        print('-'*20+f'\ncity name: {cityName} \ntemprtue: {weatherDict[cityName]['temperature']}\nhumidity: {weatherDict[cityName]['humidity']}\nWeather Condition: {weatherDict[cityName]['weatherCondition']}\nUpdated Date: {weatherDict[cityName]['date']}\n'+'-'*20 )
    else:
        print("invalid city name")




def queryCity():
    user_query=int(input("please enter the operation Number you want to do such as \n1:update\n2:delete\n Enter a number:  "))

    opreation='update' if user_query==1 else 'delete'
    cityName=input("please Enter City Name: ")
    if opreation=='update':
        try:
            temperature:str=input("Please Enter Temperature in Celisus: ")
            humidity:str=input("Please Enter humidity (eg. high mid low): ")
            weatherCondition:str=input("Please Enter weather condition: ")
            date:str=input("please Enter the data (eg. 2024/5/5) : ")
            weatherDict[cityName]={'temperature':temperature,'humidity':humidity,'weatherCondition':weatherCondition,'date':date}
    
            print("Scussfuly updated")
        except:
            print("something went wrong")
    elif opreation=='delete':
        try:
            del weatherDict[cityName]
            print("Succesfully deleted")
        except:
            print("something went wrong!")
    else: 
        print("Invalid operation name!!")

userInterface() #calling userInterface method to display the mune .
        

