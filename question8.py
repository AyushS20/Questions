# Defining Fibonacci Series
def Fibo_Series():
    n = int(input("Enter How many numbers in the Series:  "))
    a, b = 0, 1
    if n < 0 :
        print("Try using Positive Whole Numbers ONLY :)")
    elif n == a:
        print(a)
    elif n > a:
        print(a, end='  ')
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
            print(b, end='  ')

Fibo_Series()
