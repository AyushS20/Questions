def revers(): 
    n = int(input("Enter a Number:    "))
    rev = 0
    sum = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        sum = sum + a
        n = n // 10
    return ("Reverse of this Number is " + str(rev) + " and Sum of Digits of reversed number is " + str(sum))
revers()
