import json

# to change json to py
student ='{"name":"Alex","age" :25,"isStudent":true,"Skills":["Python","SQL"],"address":{"city":"Mumbai","pincode":400001}}'
s=json.loads(student)
print(s)

print(s["address"])
print(s["address"]["city"])
print(s["Skills"][1])
print(type(student))


# to change py to json
students ={"name":"Alex","age" :25,"isStudent":True,"Skills":["Python","SQL"],"address":{"city":"Mumbai","pincode":400001}}
stu=json.dumps(students)
print(stu)
print(type("isStudent"))