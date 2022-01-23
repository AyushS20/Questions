# Taking the inputs for size of series 
size = int(input("Enter the size of the series:  "))
i = 1
while(i <= size): # first loop.
   j = i
   while(j >= 1): # inner loop.
       print(j, end = ' ')  # print the series.
       j = j - 1
   i = i + 1
   print("") # for line changes.
    
