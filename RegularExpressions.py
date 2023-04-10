# re is the python module 
    import re
# Functions
    re.compile(pattern, flags=0)  - reuse is more efficient
    re.search(pattern, string, flags=0) - Scan through string looking for the first location
    re.match(pattern, string, flags=0) -  only match at the beginning of the string and not at the beginning of each line.
    Note: want to locate a match anywhere in string, use search()
    re.fullmatch(pattern, string, flags=0) -
    re.split(pattern, string, maxsplit=0, flags=0) - Split string by the occurrences of pattern
    re.findall(pattern, string, flags=0) - Return all non-overlapping matches of pattern in string, as a list of strings or tuples.
    Examples:
    re.split(r'\W+', 'Words, words, words.')
    re.search(r'\bf[a-z]*', 'which foot or hand fell fastest')
    re.finditer(r'\bf[a-z]*', 'which foot or hand fell fastest')
    re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

#split a string into fields, but the delimiters (and spacing around them) aren’t consistent throughout the string.
    def inconsistentdelimeter(line):
        return re.split(r'[;,\s]\s*', line)
    #driver code
    line='asdf fjdk; afed, fjek,asdf, foo'
    print(inconsistentdelimeter(line))

#suppose you want to match dates specified as digits, such as “11/27/2012.”
    def dateindigit(text1):
        if re.match(r'\d+/\d+/\d+', text1):
            return True
        return False
    #driver code
    sdate='3/01/2020'
    print (dateindigit(sdate))
    
# Complete example
    prog = re.compile(pattern)
    result = prog.search(string)
    is equivalent to
        result = re.search(pattern, string)

#Remove ALL spaces in a string, even between words:
    sentence = ' hello  apple'
    sentence = re.sub(r"\s+", "", sentence, flags=re.UNICODE)
    #or
    sentence.replace(" ", "")

#Remove spaces in the BEGINNING of a string:

    sentence = re.sub(r"^\s+", "", sentence, flags=re.UNICODE)

#Remove spaces in the END of a string:
    sentence = re.sub(r"\s+$", "", sentence, flags=re.UNICODE)

#Remove spaces both in the BEGINNING and in the END of a string:
    sentence = re.sub("^\s+|\s+$", "", sentence, flags=re.UNICODE)

#Remove ONLY DUPLICATE spaces:
    sentence = " ".join(re.split("\s+", sentence, flags=re.UNICODE))
