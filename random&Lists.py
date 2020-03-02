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

