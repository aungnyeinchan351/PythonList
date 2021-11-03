# Python Lists
Python has a built in special data type called **List**. List are similar to array.

## Creating a list
List can be created using **[]**.
```
a = [1,2,3,4,5,9]
b = [10,20,65,98,75,12]
c = [1,3,5,7,9]
```

## Appending a list
You can append item tnto a list using **append()** method.
```
a.append(20)
print(a)
```
Output is **[1,2,3,4,5,9,20]**.

## Extending list
a list can be extended into another list using **extend()** method.
```
a.extend(c)
print(a)
```
Output is **[1, 2, 3, 4, 5, 9, 20, 1, 3, 5, 7, 9]**.

## Inserting into a list
You can insert items into list using **insert()** method. **insert()** method take two arguments. the first argument is **index** and the second argument is **value to insert**. It insert the value(the second argument) into the list at the given index(the first argument). The index of the value at the position where the new value is inserted be **original index + 1**
```
a.insert(5, 10)
print(a)
```
Output is **[1, 2, 3, 4, 5, 10, 9, 20, 1, 3, 5, 7, 9]**.

## Removing from a list
Items in a list can be removed using remove using **remove()** method. By giving the item to remove as a parameter to **remove()** method, the item can beremoved. If item you give is not exit in the list, it can't be removed and raise a **ValueError**.
```
b.remove(65)
print(b)
try:
    b.remove(66)
except ValueError:
    print("ValueError: list.remove(x): x not in list")
```
Output is **
[10, 20, 98, 75, 12]
ValueError: list.remove(x): x not in list**.

## Removing items from the list using index
You an remove items from a list be knowing index of them. If you want to remove the item in place of index 2, give th index of item (2) to **pop()** method. The item at that index will be removed by **list.pop()** method. If the index is not in the list, it eill raise an error.
```
b.pop(2)
print(b)
try:
    b.pop(6)
except:
    print("Out of index.")
```
Output is 
**[10, 20, 75, 12]
Out of index.**

## Negative indexing
Items in the list can be accessed with negative index. the last index of every list is -1 and -2 is the second last index. 
```
print(a[-1])
```
Output is **9**.

## Removeing all item from the list
You can remove all item from the list by using **clear()** method.
```
a.clear()
print(a)
```
Output is **[]**.

## count number of times an item appear in a list
You can count the number of times an item appear in the list with **count()** method. **count()** method get the item value as the parameter and return the number of times that item in the list
```
times = b.count(12)
print(times)
```
Output is **1**.

## Sorting item tin the list
Item in the list can be sort using **sort()** method. Normally, **sort()** method doesn't take any argument and sort in ascending order. But, it can take two argument **key** and **reverse**. 
**reverse = True** will sort in descending order.
**reverse = False** will sort in ascending order.
If there is no argument in sort() method, reverse is false.
```
c.sort(key=None, reverse=False)
print(c)
c.sort(key=None,reverse=True)
print(c)
```
Output is 
**[1, 3, 5, 7, 9]
[9, 7, 5, 3, 1]**

You can get the source code of this tutorial at [list_tutorial.py].

Follow me on [Facebook](https://www.facebook.com/zinyaw3063)

Follow me on [GitHub](https://www.github.com/aungnyeinchan351)

contact me on [Email](mailto:aungnyeinchan3063@protonmail.com)
