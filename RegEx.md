
# re functions and Regular expressions: <br>
English sentences, or e-mail addresses, or TeX commands, or anything you like.  
You can then ask questions such as “Does this string match the pattern?”  

**re.search(pattern, string, flags=0)**
**re.match(pattern, string, flags=0)**
Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.  
If you want to locate a match anywhere in string, use search() instead.   
**re.fullmatch(pattern, string, flags=0)**   
If the whole string matches the regular expression pattern, return a corresponding match object.   
Return None if the string does not match the pattern; note that this is different from a zero-length match.   
**re.split(pattern, string, maxsplit=0, flags=0)**    
Split string by the occurrences of pattern. If capturing parentheses are used in pattern,then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero at most maxsplit splits occur,and the remainder of the string
is returned as the final element of the list.     
**re.findall(pattern, string, flags=0)**   
**re.sub(pattern, repl, string, count=0, flags=0)**    
**re.subn(pattern, repl, string, count=0, flags=0)**    <br>

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

# Special Sequences:   

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning: <br>  
\d	Returns a match where the string contains digits (numbers from 0-9)    
\b	Returns a match where the specified characters are at the beginning or at the end of a word   
\s	Returns a match where the string contains a white space character  
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) <br> 
\Z - Matches if the specified characters are at the end of a string   

Note : If we used the capital letter in above patterns then it will complement the above matching sequence 
