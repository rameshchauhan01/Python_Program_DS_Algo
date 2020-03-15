import unittest
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
