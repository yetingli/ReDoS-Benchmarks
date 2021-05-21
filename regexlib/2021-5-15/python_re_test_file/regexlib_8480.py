# 8480
# (http://|)(www\.)?([^\.]+)\.(\w{2}|(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum))$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"http://"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """(http://|)(www\.)?([^\.]+)\.(\w{2}|(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "http://" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")