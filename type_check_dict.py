person = {
"name": "Dharma",
"age": 32,
"location" : "Toronto"
}
print(type(person))
print(type(person["name"]))
print(type(person["age"]))

print(person["name"])
print(person["age"])
print(person["location"])

print("age" in person)

person["age"] = 31
print(person["age"])


person.update({"hair_color": "Black"})
print(person)

person["eye_color"] = "brown"
print(person)

person.pop("hair_color")
print(person)

person.popitem()
print(person)

del person["age"]
print(person)

person.clear()
print(person)

person = {
"name": "Dharma",
"age": 32,
"location" : "Toronto"
}

person.update({"hair_color": "Black"})
print(person)

person["eye_color"] = "brown"
print(person)