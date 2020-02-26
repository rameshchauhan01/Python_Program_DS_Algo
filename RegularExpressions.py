import re
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