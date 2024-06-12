phone={"0568323222": "Amal" , 
       "0522222232": "Mohammed" , 
       "0532335983": "Khadijah" , 
       "0545341144": "Abdullah", 
       "0545534556": "Rawan" ,
       "0560664566": "Faisal",
       "0567917077": "Layla"}

number = input("plase enter number :")
if len(number) == 10 and number.isdigit()==True :
  if number in phone :
    print(phone[number])
  else:
    print("Sorry, the number is not found")
else:
  print("This is invalid number")