#list
l = ["Bob", "Rolf", "Anne"]
#can't edit tuple
t = ("Bob", "Rolf", "Anne")
#sets can't have duplicate elements, the order can change
s = {"Bob", "Rolf", "Anne"}

#subscript notation, works for lists and tuples only:
print(l[0])
print(t[2])

l[0]="Olesia"
print(l)

l.append("Mike")
print(l)

l.remove("Rolf")
print(l)

s.add("Smith")
print(s)
