# info = {
#         "name" : "apnacollege",
#         "subjects": ["Python", "C", "Java"],
#         "topics" : ("dict", "sets"),
#         "age" : 35,
#         "is_adult": True,
#         "marks": 94.4
# }
# print(info)
# print(type(info))
# info["name"] = "shradha"
# info["age"] = 23
# info["location"] = "india"
# info["location"] = "japan" #overwrite the previos assign value

# print(type(info["marks"]))

# null_dict = {}
# print(null_dict)
# print(type(null_dict))
# null_dict["name"] = "hello" #null dictionary me add
# print(null_dict)


# student = {
#     "name" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }
# print(student["subjects"])
# print(student["subjects"]["chem"])
# print(student.keys())
# print(list(student.keys())) #type casting, function
# print(student.values())
# pairs = list(student.items()) # all keys&values pairs as tuples
# print(pairs[0])
# print(pairs[1])
# print(student["name"])
# print(student.get("name"))
# print("before")
# print(student["name2"])
# # print(student.get("name2"))
# print("after")
# student.update({"name" : "hello"}) #agr key same hua to update vrna last me add
# student["name2"] = "apnacollege"
# student.update({"name3":"apnacollege"})
# a = {"city": "mumbai", "home": "delhi"}
# student["new"] = a
# print(student)
# student.update(a)
# print(student)
# set = set()
# print(set)
# print(type(set))

# collection = set ()
# collection.add(1)
# collection.add(2)
# collection.add("apnacollege")
# collection.add((1,2,3))
# print(len(collection))
# print(collection)

a = {"hello", "world", "yoyo", "poco"}
b = {"wassup", "fine", "poco","yoyo"}
c = a.intersection(b)
print(c)