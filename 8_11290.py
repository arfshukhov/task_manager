from itertools import *

aplha = "0123456789abcdef"

words = ["".join(x) for x in product(aplha, repeat=4)]

cnt = 0
for i in words:
    if i.count("9") == 1 and i[0] != "0":
        for x in "02468ace":
            i = i.replace(x, "n")
        for x in "13579bdf":
            i = i.replace(x, "p")
        if "nn" not in i and "pp" not in i: cnt +=1

print(cnt)
