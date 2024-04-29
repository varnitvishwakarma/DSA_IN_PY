from array import *

array1=array("i",[1,2,3,4,5,6,7])
array2=array("d",[1.2,1.3,1.4,1.5])

print(array1)
print(array2)

#insertion at end (time complexity O(1))
array1.insert(7,8)
print(array1)


#insertion at beggning (time complexity O(n))
array1.insert(0,0)
print(array1)

#insertion at mid (time complexity O(n))
array1.insert(2,5)
print(array1)
