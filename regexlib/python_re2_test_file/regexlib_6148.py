# 6148
# <(\w+)(\s(\w*=".*?")?)*((/>)|((/*?)>.*?</\1>))
# EXPONENT
# nums:5
# EXPONENT AttackString:"<1"+"\t0="""*32+"! _1_EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """<(\w+)(\s(\w*=".*?")?)*((/>)|((/*?)>.*?</\1>))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<1" + "\t0=\"\"" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")