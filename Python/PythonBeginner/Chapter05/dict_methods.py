marks= { 
        "Ganesh" : 100, #here we use key and value pair for storing data
        "gajanan" : 75, 
        "abhi": 50
}
print(marks.values()) 
print(marks.keys())
print(marks.items())

marks.update({"Ganesh" : 99}) #use for  updating 

#we can also use .update for adding any key value pair in the dictionary
marks.update({"narayan": 22})
print(marks)

print(marks.get("Ganesh")) #prints none if not found
print(marks["Ganesh"]) #gives error if not found

print(marks.clear()) #clear the dict
# print(marks)

