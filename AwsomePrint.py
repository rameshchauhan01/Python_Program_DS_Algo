import os
"""
Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)
Parameters:
value(s) : Any value, and as many as you like. Will be converted to string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

"""
#Call any function and pass it any values
print('My name is', os.getlogin(), 'and I am', 42)
#separating the values
print('', 'home', 'user', 'documents', sep='/')
#One more interesting example could be exporting data to a comma-separated values (CSV) format:
print(1, 'Python Tricks', 'Dan Bader', sep=',')
#Finally, the sep parameter isn’t constrained to a single character only. You can join elements with strings of any length:
print('node', 'child', 'child', sep=' -> ')
#To disable the newline, you must specify an empty string through the end keyword argument:
print('Checking file integrity...', end='')
print('ok')

#Be careful about joining elements of a list or tuple. below code run with Typeerror
print(' '.join(['jdoe is', 42, 'years old']))
#It’s safer to just unpack the sequence with the star operator (*) and let print() handle type casting:
print(*['jdoe is', 42, 'years old'])

"""Looping over lines in a text file preserves their own newline characters, which combined with the print() function’s default
# behavior will result in a redundant newline character:
with open('file.txt') as file_object:
   for line in file_object:
        print(line)

>> values = ['jdoe', 'is', 42, 'years old']
>>> print ' '.join(map(str, values))
"""
"""
Unbuffered is self-explanatory, that is, no buffering is taking place, and all writes have immediate effect. 
A line-buffered stream waits before firing any I/O calls until a line break appears somewhere in the buffer, 
whereas a block-buffered one simply allows the buffer to fill up to a certain size regardless of its content. 
Standard output is both line-buffered and block-buffered, depending on which event comes first.
On the other hand, buffering can sometimes have undesired effects as you just saw with the countdown example.
 To fix it, you can simply tell print() to forcefully flush the stream without waiting for a newline character in the buffer 
 using its flush flag:
print(countdown, end='...', flush=True)
"""

"""Printing the custom data type:Normally we deal with strings and numbers  but if you want to print your own abstract data types
 then import below modules
from collections import namedtuple
from dataclasses import dataclass
@dataclass
"""

"""debugging:
 print debugging or caveman debugging
 def average(numbers):
...     print('debug1:', numbers)
...     if len(numbers) > 0:
...         print('debug2:', sum(numbers))
...         return sum(numbers) / len(numbers)
...
>>> 0.1 == average(3*[0.1]) 

A crude debugger that runs in the terminal, unsurprisingly named pdb for “The Python Debugger,” is distributed as
part of the standard library. This makes it always available, so it may be your only choice for performing remote debugging.
Perhaps that’s a good reason to get familiar with it.

However, it doesn’t come with a graphical interface, so using pdb may be a bit tricky. 
If you can’t edit the code, you have to run it as a module and pass your script’s location:

python -m pdb my_script.py
def average(numbers):
    if len(numbers) > 0:
        breakpoint()  # Python 3.7+
        return sum(numbers) / len(numbers)
"""
"""Thread safe Printing:
Thread safety means that a piece of code can be safely shared between multiple threads of execution. The simplest strategy 
for ensuring thread-safety is by sharing immutable objects only. If threads can’t modify an object’s state, 
then there’s no risk of breaking its consistency.

Another method takes advantage of local memory, which makes each thread receive its own copy of the same object. That way,
 other threads can’t see the changes made to it in the current thread.

But that doesn’t solve the problem, does it? You often want your threads to cooperate by being able to mutate a shared resource.
 The most common way of synchronizing concurrent access to such a resource is by locking it. 
This gives exclusive write access to one or sometimes a few threads at a time.

However, locking is expensive and reduces concurrent throughput, so other means for controlling access have been invented, 
such as atomic variables or the compare-and-swap algorithm.

Printing isn’t thread-safe in Python. The print() function holds a reference to the standard output, 
which is a shared global variable.In theory, because there’s no locking, a context switch could happen 
during a call to sys.stdout.write(), intertwining bits of text from multiple print() calls.
"""
