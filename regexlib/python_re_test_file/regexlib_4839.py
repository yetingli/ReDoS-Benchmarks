# 4839
# ^[a-zA-Z0-9]+([a-zA-Z0-9\-\.]+)?\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU)$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"a"+"0"*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^[a-zA-Z0-9]+([a-zA-Z0-9\-\.]+)?\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + "0" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")