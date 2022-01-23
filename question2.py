# Question 2 (a)
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
    
# Question 2 (b)
# Asking the User for input of rows
n = int(input("Enter no of rows: "))
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(end=' ')
    for j in range (1, i+ 1):
        print(j, end='')
    for j in range (i-1, 0, -1):
        print(j, end='')
    print()
for i in range (1,n):
    for j in range(1, i+1):
        print(end=' ')
    for j in range (1, n-i):
        print(j, end='')
    for j in range (n-i, 0, -1):
        print(j, end='')
    print()
 
