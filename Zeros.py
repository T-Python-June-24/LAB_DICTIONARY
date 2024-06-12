z = [5, 0, 34, 9, 0, 13, 8]

def ZerosL(z):
    NotZero = []
    Zero = []

    for n in z:
        if n == 0:
            Zero.append(n)
        else:
            NotZero.append(n)
            
    print("The List with Zeros at the end is " , NotZero + Zero)
  
ZerosL(z)