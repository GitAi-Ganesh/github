#5. Write a program to find the sum of first n natural numbers using while loop.
#in simple way if input is 2 then 1+2 = 3 
n = int(input("enter the number :  "))
i = 1
sum =0
while (i<=n):
    sum += i
    i +=1

print(sum)