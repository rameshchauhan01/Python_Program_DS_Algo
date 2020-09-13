## Type Hinting or Anotation is Python: <br>
1. argument anotations 2. return type anotations 3.variable anotations   
**Python is dynamically typed language**, and the authors have no desire to ever make type hints mandatory(Anotations), even by convention.
The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

Type annotations should not be confused with variable declarations in statically typed languages.    
The goal of annotation syntax is to provide an easy way to specify structured type metadata for third party tools.   
## Module in python: 
a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.      
# Some Common Built in Functions     
|Function Name|Description|
|------------------|-----------|
|dir()|	Returns a list of functions are implemented in each module =>print(dir(math))|
|help()|After locating our desired function in the module, we can read more about it using the help function =>help(math.factorial)|    
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
|zip(iterator1, iterator2...)|Returns an iterator,create tupe for same index values|    
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

## String functions: 
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

## List functions:  
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

## Dictionary functions:   
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

## Tuple functions:   
|Function Name|Description|
|-------------|-----------|
|count(elmnt)|Returns the number of times a specified value occurs in a tuple|
|index(elmnt)|Searches the tuple for a specified value and returns the position of where it was found|

## Set functions:   
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

## re functions and Regular expressions: <br>
**re.search(pattern, string, flags=0)** Returns a Match object if there is a match anywhere in the string    
**re.match(pattern, string, flags=0)** re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string     
**re.split(pattern, string, maxsplit=0, flags=0)** Returns a list where the string has been split at each match     
**re.findall(pattern, string, flags=0)** Returns a list containing all matches  
**re.sub(pattern, repl, string, count=0, flags=0)** Replaces one or many matches with a string     
**re.compile(pattern, flags=0)**   Compile a regular expression pattern into a regular expression object     
**re.purge()** Clear the regular expression cache.    
**exception re.error(msg, pattern=None, pos=None)**   
**re.escape(pattern)**   Escape special characters in pattern.    
**Example:**      
prog = re.compile(pattern)     
result = prog.match(string)     
is equivalent to     
result = re.match(pattern, string)        
but using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.      

**Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.If you want to locate a match anywhere in string, use search() instead.**       
**Note:raw string literals, which are exactly the string literals marked by an 'r' before the opening quote.**           

**MetaCharacters**
are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:     
[] . ^ $ * + ? {} () \ |     
[]:Square Brackets >Set of character wish to match  
.:dot>Match any single character except new line  
^:Caret>is used to check if a string starts with a certain character  
$:Dolar>is used to check if a string ends with a certain character.   
*: Astrick or star>matches zero or more occurrences of the pattern left to it   
+:Plus>matches one or more occurrences of the pattern left to it  
?:Question mark >matches zero or one occurrence of the pattern left to it.   
{}:curly Brackets or Braces>Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.  
(): Round Brackets or Parentheses>is used to Capturea nd  group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz   
\:Back slash>Signals a special sequence (can also be used to escape special characters)   
|: Pipe >Either or     
**sets:**   
[a-e] Returns a match for any lower case character, alphabetically between a and e  
[1-4] Retuns a match of any digit between 1 and 4 is the same as [1234].  
[0-5][0-9]	Returns a match for any two-digit numbers from 00 an 59  
[^arn]	Returns a match for any character EXCEPT a, r, and n .It also behave as complement(invert)   
[^0-9] means any non-digit character  
[0-9]{2, 4} matches at least 2 digits but not more than 4 digits  
**Special Sequences:**       
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning: <br>  
\d	Returns a match where the string contains digits (numbers from 0-9)    
\b	Returns a match where the specified characters are at the beginning or at the end of a word   
\s	Returns a match where the string contains a white space character  
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) <br> 
\Z - Matches if the specified characters are at the end of a string    
**Note : If we used the capital letter in above patterns then it will complement the above matching sequence**     

