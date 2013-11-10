import os
import random
f = open("sample.txt","w")
lineno=random.randint(9*10**6,10**7)
divisor=random.randint(0,10**7)
f.write(str(lineno) + " " + str(divisor) + "\n")
for i in range(0,lineno):
    f.write(str(random.randint(0,10**9)) + "\n")
f.close()
