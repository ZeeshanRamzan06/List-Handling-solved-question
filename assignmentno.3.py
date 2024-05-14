#             -----List Handling---

'''1. Write a program to read and print elements of list.'''
my_list = ["apple","banana","orange",12]
print("This is list element",my_list)

'''2. Write a program to print all negative elements in a list.'''

my_list = [1, 2, -3, -4, -5]
for i in my_list:
  if i < 0:
    print(i)

'''3. Write a program to find sum of all list elements.'''
my_list   = [2,3,4,5,6]
sumoflist = sum(my_list)
print(sumoflist)

'''4. Write a program to find maximum and minimum element in a list.'''
my_list = [2,4,6,8,10]

max_list = max(my_list)
min_list = min(my_list)
print("The maximum element is:", max_list)
print("The minimum element is:", min_list)

'''5. Write a program to find second largest element in a list.'''

my_list = [1, 2, 3, 4, 5]
my_list.sort()
print("The second largest element is:", my_list[-2])

'''6. Write a program to count total number of even and odd elements in a list.'''

list1 = [1,2,3,4,5,6,7,8,9]
 
even_count = 0
odd_count = 0
for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

'''7. Write a program to count total number of negative elements in a list.'''

my_list = [-1,2,-3,4,-5,-23]

neg_count = 0
for num in my_list:
    if num < 0:
        neg_count += 1

print("Total number of negitive number is :",neg_count) 

'''8. Write a program to copy all elements from a list to another list.'''

list1 = ["adil","tayyab","zeeshan","saud"]
list2 =list1.copy()
print("original liat is :",list1)
print("Copied list is :",list2)

'''9. Write a program to insert an element in a list.'''
fruits = ["apple","banana","orange"]
fruits.insert(1,"mango")
print("After inserting the element the list is :",fruits)

'''10. Write a program to delete an element from a list at specified position.'''
list1 = ["apple","banana","orange","mango"]
position = int(input("Enter a position to delete: ")) 
list1.pop(position)
print("The new list is:", list1)

'''11. Write a program to count frequency of each element in a list.'''
list1 = ['a','b','c','a','a','b','c','d']
frequency = {}
for item in list1:
    if item in frequency:
       frequency[item] +=1
    else:
        frequency[item] =1
print("frequency of each element is :",frequency)

'''12. Write a program to print all unique elements in the list.'''
list1 = [1, 2, 3, 4, 5, 2, 3, 4]
unique_list = []
for i in list1:
  if i not in unique_list:
    unique_list.append(i)  
print("The unique list is:", unique_list)

'''13. Write a program to count total number of duplicate elements in a list.'''
list1 = [1, 2, 3, 4, 5, 2, 3, 4]
count = 0
for i in list1:
  if list1.count(i) > 1:
    count += 1
print("The total number of duplicate elements is:", count)

'''14. Write a program to delete all duplicate elements from a list.'''

list1 = [1, 2, 3, 4, 5, 2, 3, 4]
unique_list = []
for i in list1:
  if i not in unique_list:
    unique_list.append(i)
print("The unique list is:", unique_list) 

'''15. Write a program to merge two list to third list.'''
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = list1 + list2
print("The merged list is:", list3)

'''16. Write a program to find reverse of a list.'''
list1 = [1,2,3,4,5,6]
list1.reverse()
print("The reverse list is :",list1)

'''17. Write a program to put even and odd elements of list in two separate list.'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
odd_list = []
for i in list1:
  if i % 2 == 0:
    even_list.append(i)
  else:
    odd_list.append(i)
print("The even list is:", even_list)
print("The odd list is:", odd_list)


'''18. Write a program to search an element in a list.'''
list = [1, 2, 3, 4, 5]
element = int(input("Enter a element to search: "))
if element in list:
  print("The element is found in the list")
else:
  print("The element is not found in the list")

'''19. Write a program to sort list elements in ascending or descending order.'''
list1 = [1, 2, 3, 5, 4]
list1.sort()
print("The sorted list is:", list1)

'''20. Write a program to sort even and odd elements of list separately.'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
odd_list = []
for i in list:
  if i % 2 == 0:
    even_list.append(i)
  else:
    odd_list.append(i)
even_list.sort()
odd_list.sort()
print("The even list is:", even_list)
print("The odd list is:", odd_list)

''' 21. Write a program to left rotate a list.'''
list1 = [1, 2, 3, 4, 5]
list1.append(list1.pop(0))
print("The left rotated list is:", list1)


'''22. Write a program to right rotate a list.'''
list1 = [1, 2, 3, 4, 5]
list1.insert(0, list1.pop())
print("The right rotated list is:", list1)