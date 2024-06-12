
phone_book = {"Amal": "0568323222", "Mohammed": "0522222232","Khadijah": " 0532335983 ", "Abdullah"  : "0545341144" , "Rawan"   : "0545534556" , "Faisal"  : "0560664566" ,
 "Layla"   : "0567917077 "}

num=input("Please enter the number: ")

if len(num) < 10 or not num.isdigit():
    print("This is invalid number")
    exit()
else: 
    for name, number in phone_book.items():
      if number == num:
          print(f"The number is owned by ({name})")
          exit()

print ("Sorry, the number is not found")
