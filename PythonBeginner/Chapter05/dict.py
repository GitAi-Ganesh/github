marks= { 
        "Ganesh" : 100, #here we use key and value pair for storing data
        "gajanan" : 75, 
        "abhi": 50
}

print (marks["Ganesh"])
print(marks.values())
print(marks.keys())
print(marks.items())


marks.update({"Ganesh" : 99}) #use for  updating 
print(marks)