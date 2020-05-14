#### Python Data Type: Mainly seven data type are exist in python
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''
### List, List Stack, List Queue, List Tree, List Graph
#associating#formate the list values using comprehension
L1 = [4,2,3]
L2=['a','b']
L3=['{}{}'.format(x, y) for y in L1 for x in L2]
print(L3) #['a4','b4','a2','b2','a3','b3']

##sort the second items in the list contains tuple
# with sort function
def Sort_list(l):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    l.sort(key=lambda x: x[1])
    return l
#with sorted function
def Sorted_list(l):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    return (sorted(l, key=lambda x: x[1]))

l1 = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
# printing the sorted list of tuples
print(Sort_list(l1))
l2=[(3,4,2),(6,1,3),(5,2,8)]
print(Sorted_list(l2))
#Swap the list wihtout using third variable,#It is also called the packing and unpacking
l1,l2=l2,l1

#append all zeros at the end  of array
def moveZeros(arr):
    return [nonZero for nonZero in arr if nonZero != 0] + [Zero for Zero in arr if Zero == 0]
# creating the list using the iterator it can be usefull to pass the different size list in unit test
List = []
# Adding elements to the List
# using Iterator
for i in range(4):
    List.append(i)
    print (List)
# Adding Tuples to the List
List.append((8, 9))
print("\nList after Addition of a Tuple: ")
print(List)

# Print the multiplication table
n=10
for i in range(1,11):
 print('{}*{}={}'.format(n,i,n*i))
 # or print("%d*%d=%d" %(n,i,n*i))
##Python | Add similar value multiple times for list,string,tuple

# Method 1: Using * operator
res = (3,) * 5
print ("The filtered list is : " + str(res)) #The filtered list is : (3, 3, 3, 3, 3)

#Method #2 : Using extend() + list comprehension
res = []
res.extend([3 for i in range(5)])
print("The filtered list is : " + str(res))

#Method #3 : Using extend() + itertools.repeat()
from itertools import repeat
res = []
res.extend(repeat(3, 5))
print("The filtered list is : " + str(res))
### Strings
#Use operators with strings:
#1)+ used to cancatenete or join the strings e.g >>> print ("Hi Ramesh"+'!!!') #Hi Ramesh!!!
#2)* multiplication operator represent the replication of the string. if n is negative or zero it returns the blank
 #e.g: string="Day One!"
 #>>> print(n*string) # Day One!Day One!Day One!.....n times
 #>>> print(n*'Hi Ramesh') # Hi RameshHi RameshHi Ramesh ....n times
 #>>> print(n*['Hi Ramesh'])# [Hi Ramesh,Hi Ramesh,Hi Ramesh,....n tims]
 #>>> print(n*string,n*'Hi Ramesh',n*['Hi Ramesh'])
#3)in and not in membership operator returns the boolean values
#e.g >>> s='Hi how is your day?'
#print('?' in s ) # True
#print ('Hi How' not in s) #True
#4)Access and extract portions of strings :  slicing is used
#5)Use built-in Python functions with characters and strings
#6)Use methods to manipulate and modify string data : Most frequent split and join function are used.
## string reverse ways:: input:'Today is mothers day' Output: yad srehtom si yadoT
#Using slice
def reverse_slice(s):
    return s[::-1]
#Using loop
def reverse_loop(s):
  str = ""
  for i in s:
    str = i + str
  return str
#using recursion
def reverse_rec(s):
    if len(s) == 0:
        return s
    else:
        return reverse_rec(s[1:]) + s[0]
#Using Reversed function
def reverse_reversed(string):
    string = "".join(reversed(string))
    return string
# Using List reverse
def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)
#Note: Slice is efficient than others approaches

##String reverse in different type using slice
#Python reverse string input:'Today is mothers day' Output: yadoT si srehtom yad
def sReverse_without_place_swap(s):
    words=s.split(" ")
    reversen= [i[::-1] for i in words]
    final=' '.join(reversen)
    return final
#Python reverse string input:'Today is mothers day' Output: day mothers is Today
def sWordPlaceSwap(s):
    words = s.split(" ")
    reversen = words[::-1]
    final = ' '.join(reversen)
    return final

## number(integer) reverse:: input:123 output:321
# Integer reverse using integer divide
def numberRev(n):
    result=''
    oldn=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10 +rem
        n=n//10
    #return rev
    print(n)
    print(oldn)
    print(rev)
    if oldn==rev:
        result='Magical'
    else:
        result='Nonmagical'
    return result
#integer reverse using the conersions
def number_reverse_conversions(n):
    s=str(n)
    rev=s[::-1]
    revers=int(rev)
    return revers
   
### List Vs Tuple
'''
import dis :The dis module disassembles the byte code for a function
e.g:dis.dis(function
1.accessing an element generates identical code for both,
2.assigning a tuple is much faster than assigning a list.
3.creating a tuple is faster than List.
4.Lists have several built-in methods compare to tuple
5.List is more error prone compare to tuple due to mutable nature
6.List consume more memory than tuple
'''
##
# Yield successive n-sized
# chunks from given list.
def divide_chunks(l, n):
    #l is the list
    for i in range(0, len(l), n):
        yield l[i:i + n]
        """The yield keyword enables a function to comeback where it left off when it is called again. 
        This is the critical difference from a regular function. 
        A regular function cannot comes back where it left off. 
        The yield keyword helps a function to remember its state."""
# Driver code
my_list = [2,1,4,3,5,6,7,8]
n = 3
x = list(divide_chunks(my_list, n))
print(x)
