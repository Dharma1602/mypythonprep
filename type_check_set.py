simpleSet = {4,2,5,8,1}
print(type(simpleSet))

for x in simpleSet:
  print(x)

simpleSet.add(10)
print(simpleSet)

simpleSet.remove(10)
print(simpleSet)

#eliminates the duplicates

simpleSet2 = {1, 2,2, 3, 3, 3, 4, 4, 4,4, 5,5,5,5,5 }
print(simpleSet2)


#set can be used for mathematic set operations
#uninon
setA = {1, 2, 3, 4, 5, 6}
setB = {4, 5, 6, 7, 8, 9}
print(setA.union(setB))
print(setB.union(setA))

#intersection
print(setA.intersection(setB))
print(setB.intersection(setA))

#differece
print(setA.difference(setB))
print(setB.difference(setA))


print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))