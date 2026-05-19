student = {
    "name" : "snehith",
    "age"  : 22,
    "marks": 95
}

d1 = student
print (d1)
student["id"] =1
print (d1)

d1 = student.copy()
student["city"] = "Hyd"     # change on student
print(d1) 
print(student)


'''
student["name"] = "durga"
print (student)

print(type(student))
print(student.get("type", "not found"))
#print(student["type"])
'''