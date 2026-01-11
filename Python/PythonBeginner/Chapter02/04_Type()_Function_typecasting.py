# by using type function we can check the data type of the variable
a = 23
b = type(a)
print (b)

c = 222.22
d =type(c)
print (d)

e = "is this it"
f = type(e)
print (f)
 
# Now we will perform typecasting
#typecasting means changing the data type of the of the variable

integer = 24 # this is an integer 
g = float(integer) # here we converted our integer variable to the float
h= type (g)
print("the data type is", h)

float = 22.222
i = int(float)
j = type(i)
print ("here we converted float into :", j)

nu = 23 # this is an integer 
k = str (nu) # we converted integer to the string
l = type (k)
print (l)
