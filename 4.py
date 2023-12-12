#!/usr/bin/env python3

import re

data = open("ref4.txt").readlines()

calc = []
for row in data:
    row = row.strip().split(":")[1]
    cards = row.split("|")
    my_card = set(re.split("\s+", cards[0].strip()))
    their_card = set(re.split("\s+", cards[1].strip()))
    res = their_card.intersection(my_card)
    if len(res):
        # calc.append(res)
        calc.append(int(2 ** len(res) / 2))

print(sum(calc))
# print(calc)
