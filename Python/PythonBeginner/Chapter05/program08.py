# . If languages of two friends are same; what will happen to the program in problem
# 6?


dic={}

n= input("enter the name of the 1st friend  ")
lang= input("enter the language of 1st friend  ")
dic.update({n:lang})

n= input("enter the name of the 2nd friend  ")
lang= input("enter the language of 2st friend  ")
dic.update({n:lang})

print(dic)

# if the values re same then it will print both differnt key value pair