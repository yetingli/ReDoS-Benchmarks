# 3628
# ^ *([AaBbCcEeGgHhJjKkLlMmNnPpRrSsTtVvXxYy]\d[a-zA-Z]) *-* *(\d[a-zA-Z]\d) *$|^ *(\d{5}) *$|^ *(\d{5}) *-* *(\d{4}) *$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"A1a"+" "*10000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^ *([AaBbCcEeGgHhJjKkLlMmNnPpRrSsTtVvXxYy]\d[a-zA-Z]) *-* *(\d[a-zA-Z]\d) *$|^ *(\d{5}) *$|^ *(\d{5}) *-* *(\d{4}) *$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "A1a" + " " * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")