simplelist = ["Red", "Green", "Blue", 4, 5, 6]
print(simplelist)
print(type(simplelist))
print(type(simplelist[5]))

print("simplelist[4] =", simplelist[4])
print("simplelist[0:4] =", simplelist[0:4])
print("simplelist[4:] =", simplelist[4:])
print("simplelist[2:] =", simplelist[2:])
print("simplelist[-1] =", simplelist[-1])
simplelist[2] = 3
print("value did changed", simplelist)
simplelist.insert(6, "new value")
print("New value added to list", simplelist)
simplelist.pop(2)
print("One item removed from the item by index", simplelist)
