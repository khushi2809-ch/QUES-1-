#create a list of 10no with repeated numbers
mylist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#displaying list
print("numbers are : ")
print(mylist)
print("---------------------")
# to delete element from index (last)
mylist.pop()
print("after deleting element from index 5 : ")
print(mylist)
mylist.pop()
print("after deleting last element : ")
print(mylist)
print("------------------")
# to delete element 3
mylist.remove(3)
print("after deleting element 3 : ")
print(mylist)
print("--------------------")


'''output:  
numbers are : 
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

---------------------
after deleting element from index 5 :                           
[1, 2, 3, 4, 5, 1, 2, 3, 4]
after deleting last element :           
[1, 2, 3, 4, 5, 1, 2, 3]
------------------
after deleting element 3 :
[1, 2, 4, 5, 1, 2, 3]
-------------------
'''

