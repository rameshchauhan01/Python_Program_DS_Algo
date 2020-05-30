
### OS Module
import os
print(os.path.dirname(__file__))  # Return  path of current working dir parent node =>C:/Users/DELL/PycharmProjects/api-ui-mobile-automation-frameworks/screens
print(os.path.abspath("slenium_automation.yml")) # Return full file dir path =>C:\Users\DELL\PycharmProjects\api-ui-mobile-automation-frameworks\screens\slenium_automation.yml
print(os.path.basename("C:/Users/DELL/PycharmProjects/api-ui-mobile-automation-frameworks")) # Return the the end separator value =>api-ui-mobile-automation-frameworks
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print( os.path.join(ROOT_DIR, 'configuration.conf')) #append a file name in path
print( os.path.abspath('..\\')) # return parent to parent dir path
print( os.path.abspath('..\\ostest.py')) #append the file name in parent to parent dir
print( os.path.realpath('..')) # return parent to parent dir path

print(os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 3)[0]) #Return the 3 level up path forn current working dir
print(os.environ)#all the directories of all user environment variables
print(os.listdir()) #returns a list of files and the folders in the current directory.

##os.stat() function returns the list of details about the file or the directory name given in the argument
print(os.stat('ostest.py').st_mtime)
print(os.stat('ostest.py').st_size)

##os.walk():Traverses and produces the directory path, the direct within that path and the files within that path. It is useful to keep track of all the directories.
#return 3 list
for dirpath, dirname, filename in os.walk('C://Users//DELL//PycharmProjects//Selenium'):
    print('Current path: ',dirpath)
    print('Directories: ', dirname)
    print('Files: ', filename)
##Remove the file/dir from the path
print(os.remove('C://Users//DELL//PycharmProjects//api-ui-mobile-automation-frameworks//.github//workflows//tes34')) 

## find all files in a directory with extension .txt ?
for file in os.listdir("F:/"):
    if file.endswith(".txt"):
        print(os.path.join("F:/", file)) # it print the the file path
        print( file) #It print only the files name
#It can also use the glob module to achieve the same:
import glob
os.chdir("F:/")
for file in glob.glob("*.txt"):
    print(file)

#to traverse directory, use os.walk:
for root, dirs, files in os.walk("F:/"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))
### math module
import math
print(math.sqrt(15)) # returns the exact number till last float same as fabs(x)
print(math.fmod(17,5)) # Returns the remainder when x is divided by y 17/5=>2.0  Note: Modulus operator returns the pure integer value while fmod returns the float
print(math.pow(3,2)) #3 to the power 2 =>9.0
print(math.trunc(5.9)) #Integer =>5
print(math.isnan(3)) #Returns True if x is a Not a Number =>False
print(math.factorial(3)) # =>6
print(math.floor(3.9)) # Lover integer value to number =>3
print(math.ceil(3.9)) #Greater integer to number =>4

### Sys module
