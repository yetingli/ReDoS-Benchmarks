# 3648
# https?://[\w./]+\/[\w./]+\.(bmp|png|jpg|gif)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"http://"+"/."*5000+"! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """https?://[\w./]+\/[\w./]+\.(bmp|png|jpg|gif)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://" + "/." * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")