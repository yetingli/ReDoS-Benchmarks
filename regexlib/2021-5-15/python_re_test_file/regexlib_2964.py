# 2964
# (?:(?<scheme>[a-zA-Z]+)://)?(?<domain>(?:[0-9a-zA-Z\-_]+(?:[.][0-9a-zA-Z\-_]+)*))(?::(?<port>[0-9]+))?(?<path>(?:/[0-9a-zA-Z\-_.]+)+)(?:[?](?<query>.+))?
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"A"*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """(?:(?<scheme>[a-zA-Z]+)://)?(?<domain>(?:[0-9a-zA-Z\-_]+(?:[.][0-9a-zA-Z\-_]+)*))(?::(?<port>[0-9]+))?(?<path>(?:/[0-9a-zA-Z\-_.]+)+)(?:[?](?<query>.+))?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")