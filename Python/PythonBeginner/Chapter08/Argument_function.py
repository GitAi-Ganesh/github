# Argument function
def user(name):  # function with argument
    print("Good day,", name)

user("ganesh")


def new_user(name, age): # function with multiple arguments
    print("Hello", name, "you are", age, "years old.")
    
new_user("abhi", 21)


#using return statement
def new_user(name, age): # function with multiple arguments
    print("Hello", name, "you are", age, "years old.")
    return 21  #IN RETURN STATEMENT WE CAN RETURN ONLY ONE VALUE

a = new_user("abhi", 21)


print(a)


    