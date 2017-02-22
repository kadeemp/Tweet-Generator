import sys
import random

x = int(sys.argv[1])
resultString = ""
f = open("/usr/share/dict/words", "r")
content = f.readlines()

content = [i.rstrip("\n") for i in content]

if sys.argv[1] is not None:
    while x != 0:
        resultString += random.choice(content)
        resultString += " "
        x-=1
    if x == 0:
        resultString += "."

print resultString
g.close()
