# Write a Python program to reverse the order of the items in the array.
from array import *
arr=array('i',[1,2,3,4,5,6,7,8,9])
print("the original order of the array is:\n")
for i in arr:
    print(i,end=" ")
    
arr.reverse()

print("\nthe reversed array is: \n")
for i in arr:
    print(i,end=" ")