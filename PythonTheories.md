# Type Hinting or Anotation is Python: <br>
1. argument anotations 2. return type anotations 3.variable anotations   
**Python is dynamically typed language**, and the authors have no desire to ever make type hints mandatory(Anotations), even by convention.
The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

Type annotations should not be confused with variable declarations in statically typed languages.    
The goal of annotation syntax is to provide an easy way to specify structured type metadata for third party tools.   
# Module in python: 
a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.      
# Some Common Built in Functions     
|Function Name|Description|
|------------------|-----------|
|dir()|	Returns a list of the specified object's properties and methods|
|help()|Executes the built-in help system
|eval(expression,globals, locals)|Evaluates and executes an expression:x = 'print(55) eval(x)>>>55|
|exec(object, globals, locals)|Executes the specified code (or object)|
|min(iterable)|	Returns the smallest item in an iterable|
|max(iterable)|	Returns the largest item in an iterable|
|iter(iterable)|	Returns an iterator object|
|next(iterable, default)|	Returns the next item in an iterable|
|filter(function, iterable)|Use a filter function to exclude items in an iterable object|
|map(function, iterables)|Returns the specified iterator with the specified function applied to each item|
|enumerate(iterable, start)|Takes a collection (e.g. a tuple) and returns it as an enumerate object:L = ['apples', 'bananas', 'oranges']for idx, val in enumerate(L)print("index is %d and value is %s" % (idx, val))|
|range(start, stop, step)|Returns a sequence of numbers, starting from 0 and increments by 1 (by default)|
|zip(iterator1, iterator2...)|Returns an iterator, from two or more iterators
|reversed(iterator)|Returns a reversed iterator|
|slice(start, end, step)|Returns a slice object|
|sorted(iterable, key=key, reverse=reverse)|Returns a sorted list:You cannot sort a list that contains BOTH string values AND numeric values.|
|format(value, format)|	Formats a specified value:x = format(0.5, '%') print(x)>>>50.00000%|
|frozenset(iterable)|Returns a frozenset object|
|abs(n)|Returns the absolute value of a number|
|sum(iterable, start)|	Sums the items of an iterator|
|pow(base,exponent,modulus)|x = pow(4, 3, 5) 4*4*4 %5 print(x)>>>4 |
|divmod(divident, divisor)| Returns the quotient and the remainder when argument1 is divided by argument2:x = divmod(113, 2) print(x)>>>(56,1)|
|bin(n)|Returns the binary version of a number|
|bool(object)|	Returns the boolean value of the specified object|
|isinstance(object, type)|Returns True if a specified object is an instance of a specified object|
|issubclass(object, subclass)|	Returns True if a specified class is a subclass of a specified object|
|callable(object)|Returns True if the specified object is callable, otherwise False|
|super()|Returns an object that represents the parent class|
|setattr(object, attribute, value)|Sets an attribute (property/method) of an object|
|getattr(object, attribute)|Returns the value of the specified attribute (property or method)|

