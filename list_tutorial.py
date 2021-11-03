#Creating Lists
a = [1,2,3,4,5,9]
b = [10,20,65,98,75,12]
c = [1,3,5,7,9]

#appending a list
a.append(20)
print(a)

#Extending lists
a.extend(c)
print(a)

#Inserting an item to the list
a.insert(5, 10)
print(a)

#Removing an item from a list
b.remove(65)
print(b)
try:
    b.remove(66)
except ValueError:
    print("ValueError: list.remove(x): x not in list")

#Removing item with index
b.pop(2)
print(b)
try:
    b.pop(6)
except:
    print("Out of index.")

#Negative indexing
print(a[-1])

#Remove all item from the list
a.clear()
print(a)

#count number of times an item appear in a list
times = b.count(12)
print(times)

#Sorting item in the list
c.sort(key=None, reverse=False)
print(c)
c.sort(key=None,reverse=True)
print(c)