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