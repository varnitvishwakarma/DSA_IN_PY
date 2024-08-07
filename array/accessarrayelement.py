from array import *

array1=array("i",[1,2,3,4,5,6,7,8,9,10])


def accessElement(array,index):
    if index>=len(array):
        print("There is not any element in this index")
    else:
        print(array[index])


accessElement(array1,10)