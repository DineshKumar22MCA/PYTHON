f=open("textt.txt","w")
f.write("hello mia and sunny")
print(f)

f=open("textt.txt","a")
f.write("\n dinesh want fuck mia")
print(f)
f.close()

import os

if os.path.exists("text.txt"):
    os.remove("text.txt")