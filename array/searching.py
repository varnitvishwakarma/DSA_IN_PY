from array import *

array1=array("i",[1,2,3,4,5,6,7,8,9,10])

def search(array,element):
    for i in array:
        if i ==element:
            return array.index(element)

    return "The element does not exist in this array"



print(search(array1,10))