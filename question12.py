# Part (a): Sum of First Odd Numbers
def odd_sum():
    sum = 0
    n = int(input("Enter the Number:   "))
    for i in range (0, n + 1):
        if i % 2 == 1:
            sum += i
            print("term = ", i, ", sum till this step =", sum)
        else:
            continue
odd_sum()

# Part (b): Sum of first even numbers 
def even_sum():
    sum = 0
    n = int(input("Enter the Number:   "))
    for i in range (0, n + 1):
        if i % 2 == 0:
            sum += i
            print("term = ", i, ", sum till this step =", sum)
        else:
            continue
even_sum()

# Part (c): Sum of N Natural Numbers
def natural_n():
    n = int(input("Enter the number: "))
    sum1 = 0
    while(n > 0):
        sum1 = sum1 + n
        n = n - 1
    print("The sum of first", n, "natural numbers is", sum1)
natural_n()
