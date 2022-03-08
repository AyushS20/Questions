# defining a function to calculate LCM  
def calculate_lcm(p, q):  
    # selecting the greater number  
    if p > q:  
        gre = p  
    else:  
        gre = q  
    while(True):  
        if((gre % p == 0) and (gre % q == 0)):  
            lcm = gre
            break  
        gre += 1  
    return lcm    
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))  
