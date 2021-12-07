'''
Program: List Comprehension
Filename: listComprehension-tRaj-00.py
Author: Tushar Raj
Description: solving the list comprehension questions
Revisions: No revisions made
'''

print("List Comprehension\n\n")

###### 1. List comprehension analysis
### Code
def linc(a,b=2):
    '''
    description: adds the value of b to all elements in the list
    input: list and int data type
    output: list data type
    '''
    return [x+b for x in a if type(x) is int]
x = [1,2,'3',4]
y = linc(x)  # [3,4,6]
z = linc(x,1) # [2,3,5]
print(x) #This will print the list  x as it is
print(y) #This will give the list by increasing value by 2 except the string x[2]
print(z) #This will give the list by increasing value by 1 except the string x[2]



###### 2. the listInc() function
def listInc(a):
    '''
    description: adds 1 to each elements in the list
    input: list data type
    output: list data type
    '''
    return [i+1 for i in a if type(i) == int] #each value of the list is incremented by 1
### listInc() tests
assert listInc([7,2,4,8]) == [8,3,5,9], 'listInc failed [7,2,4,8]'
assert listInc([9,-1,0.0,5]) == [10,0,6], 'listInc failed [9,-1,0.0,5]'
print('\nlistInc is OK\n')


###### 3. the listOut() function
def listOut(a):
    '''
    description: print element of list in seperate line
    input: list data type
    output: int data type
    '''
    return [print(i) for i in a] #each value of list is printed in seperate line
### listOut() tests
listOut([7,2,'OK',8])
print()
listOut([[1,2],2.0,'$',8])
print()


###### 4. statements that move items between lists
### end of A to beginning of B
a,b = [1,2,3], [4,5,6]
b.insert(0,a.pop()) #poping out the a list value and inserting in list b
print(a,b)
### beginning of A to end of B
a,b = [1,2,3], [4,5,6] 
b.append(a.pop(0)) #poping out the a list value and inserting in list b at last
print(a,b,'\n')



###### 5a. the rotateForward() function
def rotateForward(a):
    '''
    description: rotates list by 1 in forward direction
    input: list data type
    output: list data type
    '''
    return a[len(a) - 1:len(a)] + a[0:len(a) - 1] #rotating the list by 1 position in forward direction
### rotateForward() tests
assert rotateForward([1,2,3,4]) == [4,1,2,3], 'rotateForward failed'
print('rotateForward ok\n')
###### 5a. the rotateForward() function
def rotateBackward(a):
    '''
    description: rotates list by 1 in backward direction
    input: list data type
    output: list data type
    '''
    return a[1:] + a[:1] #rotating the list by 1 position in backward direction
### rotateForward() tests
assert rotateBackward([1,2,3,4]) == [2,3,4,1,], 'rotateBackward failed'
print('rotateBackward ok\n')



###### 6. Analysis of iSort()
def iSort(x,n=2):
    '''
    description: sorts a list according to a value of n
    input: list and int data type
    output: list data type
    '''
    return sorted(x,key =lambda a:a[n]) #sorting the list and returning the value
x = [(1,'one','uno'),(2,'two','dos'),(3,'three','tres')]
print(iSort(x))
print(iSort(x,1))
print()



###### 7. Length sorting
z = ['bzz','z','cz','azzz']
z.sort(key=lambda z:len(z)) #sorting the list on basis of length
print(z,'\n')


###### 8. the backSort() function
def backSort(a):
    '''
    description: sort a list according to last letter
    input: list data type
    output: list data type
    '''
    return sorted(a,key=lambda a: a[-1]) #sorting the list on basis of last character value of each item
### backSort() tests
assert backSort(['red','yellow','blue','green','black']) == \
       ['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
print('backSort OK')


print("\n\n*** List Comprehension Ended ***\n\n")
