#!/usr/bin/env python3

import re

data = open("ref1.txt").readlines()
cpl = re.compile("[^\d]")

out = []
for row in data:
    row = row.replace("one","o1e").replace("two","t2o").replace("three","thr3e").replace("four","fo4r")
    row = row.replace("five","fi5e").replace("six","s6x").replace("seven","se7en").replace("eight","eig8t")
    row = row.replace("nine","ni9e")
    
    row = cpl.sub("", row)
    if len(row) == 1:
        num = f"{row}{row}"
    else:
        num = f"{row[0:1]}{row[-1:]}"
    print(num)

    out.append(int(num))

# print(out)
print(sum(out))
