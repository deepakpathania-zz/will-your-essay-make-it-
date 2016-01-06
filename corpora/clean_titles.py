import re
f = open('book','rw')
str = f.read()
re.sub(r".*[\x90-\xff].*", str)
f.write(str)
