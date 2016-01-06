import re
f = open('book','rw')
str1 = f.read()
str1 = re.sub(r".*[\x90-\xff].*", "",str1)
print str1

