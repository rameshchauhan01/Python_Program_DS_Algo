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