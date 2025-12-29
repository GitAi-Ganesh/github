# Recursion in Python
'''
factorial of 0 is : 1
factorial of 1 is : 1
factorial of 2 is : 2 x 1
factorial of 3 is : 3 x 2 x 1
factorial of 4 is : 4 x 3 x 2 x 1
factorial of 5 is : 5 x 4 x 3 x 2 x 1

'''

#using recursion

def factorial (n):   #recursive function
    if (n==1 or n==0):
        return 1
    return n * factorial (n-1)  #formula n! = n x (n-1)!


n = int(input("enter the factorial number: "))

print(f"the factorial of the number is {factorial(n)}")

