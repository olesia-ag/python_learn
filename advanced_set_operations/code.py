from typing import AbstractSet


friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print('local frined:', local_friends)

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print('frineds', friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print('both', both)


#BOOLEANS
print(5 == 5)
print(10 != 10)

# '==' compares if items are the same, by value; 'is' keyword compares by reference
