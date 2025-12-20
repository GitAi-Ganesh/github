# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

dic={}

n= input("enter the name of the 1st friend ")
lang= input("enter the language of 1st friend")
dic.update({n:lang})

n= input("enter the name of the 2ndfriend ")
lang= input("enter the language of 1st friend")
dic.update({n:lang})

n= input("enter the name of the 1st friend ")
lang= input("enter the language of 1st friend")
dic.update({n:lang})

n= input("enter the name of the 1st friend ")
lang= input("enter the language of 1st friend")
dic.update({n:lang})

print(dic)