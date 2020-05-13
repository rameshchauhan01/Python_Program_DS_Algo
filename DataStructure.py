# Python Data Type: Mainly seven data type are exist in python
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''

#Format
#associating the list values using comprehension
L1 = [4,2,3]
L2=['a','b']
L3=['{}{}'.format(x, y) for y in L1 for x in L2]
print(L3) #['a4','b4','a2','b2','a3','b3']

# Print the multiplication table
n=10
for i in range(1,11):
 print('{}*{}={}'.format(n,i,n*i))
 # or print("%d*%d=%d" %(n,i,n*i))

 #-----------------------------

#Python | Add similar value multiple times for list,string,tuple

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
## Reverse individual words in a sentence e.g: 'Today is monday' > 'yadoT si yadnom'
def reverse_wordInSen(s):
    news=s.split(" ")
    revs=[res[::-1] for res in news]
    nres=" ".join(revs)
    return nres
#For above code there is best approach if traversing the string from both ends

##Reverse the words in a given string or print word of string in reverse order e.g: 'Today is monday' > 'monday is Today'
def reverse_sentence(s):
    news=s.split(" ")
    revs=news[::-1]
    nres=" ".join(revs)
    return nres
#Reverse  string according to the number of words e.g: 'Today is monday' > 'monday is Today'
def reverse_sentenceNOW(s):
    news=s.split(" ")
    revs=[news[i] for i in range(len(news)) if i%2==0]
    wd=revs[::-1]
    evenRev=" ".join(wd)
    revs1=[news[i] for i in range(len(news)) if i%2!=0]
    evenRev1=" ".join(revs1)
    nres=evenRev+" "+evenRev1
    return nres

#Driver code
s='Today is monday uff'
print(reverse_wordInSen(s))
print(reverse_sentence(s))
print(reverse_sentenceNOW(s))
import unittest
class TestSentenceReverse(unittest.TestCase):

    def test_reverse_wordInSen(self):
        s1 = ''
        s2 = '1 2 3 4'
        s3 = 'Rainy day!'

        self.assertEqual(reverse_wordInSen(s1), s1)
        self.assertEqual(reverse_wordInSen(s2), '1 2 3 4')
        self.assertEqual(reverse_wordInSen(s3), 'yniaR !yad')

    def test_reverse_sentence(self):
        s1 = ''
        s2 = '1 2 3 4'
        s3 = 'Rainy day!'

        self.assertEqual(reverse_sentence(s1), s1)
        self.assertEqual(reverse_sentence(s2), '4 3 2 1')
        self.assertEqual(reverse_sentence(s3), 'day! Rainy')

if __name__ == '__main__':
    unittest.main()

#List Vs Tuple
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


import random
Start = 0
Stop = 20
limit = 5
RandomListOfIntegers = [random.randint(Start, Stop) for iter in range(limit)]
print(RandomListOfIntegers)

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

#sort the second items in the list contains tuple
#with sort function
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
#Swap the list wihtout using third variable
l1,l2=l2,l1
print (l1)
print (l2)

#append all zeros at the end  of array
def moveZeros(arr):
    return [nonZero for nonZero in arr if nonZero != 0] + [Zero for Zero in arr if Zero == 0]

# Driver function
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print(moveZeros(arr))

