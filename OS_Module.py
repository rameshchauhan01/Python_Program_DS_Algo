
#find all files in a directory with extension .txt ?
import os

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