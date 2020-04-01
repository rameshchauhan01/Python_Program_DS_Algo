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

*String functions:*   
|Function Name|Description|
|-------------|-----------|
|split(separator,maxsplit)|Splits the string at the specified separator, and returns a list :txt = "apple#banana#cherry" x = txt.split("#", 1) print(x)>>>['apple', 'banana#cherry']|
|join(iterable)|Joins the elements of an iterable to the end of the string:mylist = ["Ramesh","India" mySeparator = "," x = mySeparator.join(myDict) print(x)>>>Ramesh,India|
|format(value1, value2...)|Formats specified values in a string:Table of 3>> for i in range(1,11): x='{}*{}={}'.format(3,i,3*i)|
|strip(characters)|Returns a trimmed version of the string,Here characters is optional|
|replace(oldvalue, newvalue, count)|Returns a string where a specified value is replaced with a specified value: count is optional and default count for each occurance|
|count(value, start, end)|Returns the number of times a specified value occurs in a string: start and end are optional|
|find(value, start, end)|Searches the string for a specified value and returns the position of where it was found:start and end are optional|
|index(value, start, end)|Same as find except If the value is not found, the find() method returns -1, but the index() method will raise an exception|
|format_map(dictionary)|Formats specified values in a string for dict values:a = {'x':'John', 'y':'Wick'} print("{x}'s last name is {y}".format_map(a)) >>>John's last name is Wick|
|title()|Converts the first character of each word to upper case|
|capitalize()|Converts the first character to upper case|
|upper()|Converts a string into upper case|
|swapcase()|Swaps cases, lower case becomes upper case and vice versa|
|center()|Returns a centered string|
|endswith(value, start, end)|Returns true if the string ends with the specified value|
|islower()|Returns True if all characters in the string are lower case|
|isspace()|Returns True if all characters in the string are whitespaces|
|zfill()|Fills the string with a specified number of 0 values at the beginning|

*List functions:*   
|Function Name|Description|
|-------------|-----------|
|append(elmnt)|Adds an element at the end of the list|
|extend(iterable)|Add the elements of a list (or any iterable), to the end of the current list|
|insert(pos, elmnt)|Adds an element at the specified position|
|pop(index)|Removes the element at the specified position|
|remove(elmnt)|Removes the first item with the specified value|
|clear()|Removes all the elements from the list|
|copy()|Returns a copy of the list|
|count(elmnt)|Returns the number of elements with the specified value|
|index(elmnt)|Returns the index of the first element with the specified value|
|reverse()|Reverses the order of the list|
|sort(reverse=True|False, key=myFunc)|Sorts the list:reverse=True will sort the list descending. Default is reverse=False|


*Dictionary functions:*   
|Function Name|Description|
|-------------|-----------|
|get(keyname, value)|Returns the value of the specified key: value is optional|
|items()|Returns a list containing a tuple for each key value pair|
|keys()|Returns a list containing the dictionary's keys|
|fromkeys(keys, value)|Returns a dictionary with the specified keys and value:x = ('key1', 'key2', 'key3') y = 0 thisdict = dict.fromkeys(x, y) print(thisdict)>>>['key1': 0, 'key2': 0, 'key3': 0]|
|pop(key, defaultvalue)|Removes the element with the specified key|
|popitem()|Removes the last inserted key-value pair|
|setdefault(keyname, value)|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
|update(dictiterable)|Updates the dictionary with the specified key-value pairs|
|values()|Returns a list of all the values in the dictionary|
|clear()|Removes all the elements from the dictionary|
|copy()|Returns a copy of the dictionary|

*Tuple functions:*   
|Function Name|Description|
|-------------|-----------|
|count(elmnt)|Returns the number of times a specified value occurs in a tuple|
|index(elmnt)|Searches the tuple for a specified value and returns the position of where it was found|

*Set functions:*   
|Function Name|Description|
|-------------|-----------|
|add()|Adds an element to the set|
|clear()|Removes all the elements from the set|
|copy()|Returns a copy of the set|
|difference()|Returns a set containing the difference between two or more sets|
|difference_update()|Removes the items in this set that are also included in another, specified set|
|discard()|Remove the specified item|
|intersection()|Returns a set, that is the intersection of two other sets|
|intersection_update()|Removes the items in this set that are not present in other, specified set(s)|
|isdisjoint()|Returns whether two sets have a intersection or not|
|issubset()|Returns whether another set contains this set or not|
|issuperset()Returns whether this set contains another set or not|
|pop()|Removes an element from the set|
|remove()|Removes the specified element|
|symmetric_difference()|Returns a set with the symmetric differences of two sets|
|symmetric_difference_update()|inserts the symmetric differences from this set and another|
|union()|Return a set containing the union of sets|
|update()|Update the set with the union of this set and others|


