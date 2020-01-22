"""
Use operators with strings:
1)+ used to cancatenete or join the strings e.g >>> print ("Hi Ramesh"+'!!!') #Hi Ramesh!!!
2)* multiplication operator represent the replication of the string. if n is negative or zero it returns the blank
 e.g: string="Day One!"
 >>> print(n*string) # Day One!Day One!Day One!.....n times
 >>> print(n*'Hi Ramesh') # Hi RameshHi RameshHi Ramesh ....n times
 >>> print(n*['Hi Ramesh'])# [Hi Ramesh,Hi Ramesh,Hi Ramesh,....n tims]
 >>> print(n*string,n*'Hi Ramesh',n*['Hi Ramesh'])
3)in and not in membership operator returns the boolean values
e.g >>> s='Hi how is your day?'
print('?' in s ) # True
print ('Hi How' not in s) #True

4)Access and extract portions of strings :  slicing is used
5)Use built-in Python functions with characters and strings
6)Use methods to manipulate and modify string data : Most frequent split and join function are used.
"""
## Reverse the word in a sentence and wtite the possible unit test for the methods
def reverse_sentence(s):
    news=s.split()
    for res in news:
        revs=res[::-1]
    return revs
s='Hellow ramesh'
print(reverse_sentence(s))