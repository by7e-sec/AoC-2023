#!/usr/bin/env python3

import re

data = open("ref2.txt").readlines()
max_objs = {"red": 12, "green": 13, "blue": 14}

def mul(*args):
    print(args)
    out = 1
    for arg in args:
        out *= arg
    
    return out

valid_games = []
max_games_sum = []
for row in data:
    max_count = {"red": 1, "green": 1, "blue": 1}
    inf = row.strip().split(':')
    row_data = inf[1].strip()
    turns = row_data.split(';')
    is_failed = False
    for turn in turns:
        turn = turn.strip()
        for item in turn.strip().split(','):
            item = item.strip()
            calc = re.split("\s+", item)
            name = calc[1].strip()
            value = int(calc[0].strip())
            if max_objs[name] < value:
                is_failed = True
            if value > max_count[name]:
                max_count[name] = value

    max_games_sum.append(mul(*list(max_count.values())))
    if not is_failed:
        valid_games.append(int(inf[0][5:].strip()))

print(f"Sum of valid games: {sum(valid_games)}")
print(f"Max sum of all games: {sum(max_games_sum)}")
