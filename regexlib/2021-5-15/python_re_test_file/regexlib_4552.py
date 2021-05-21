# 4552
# (^[A-ZÀ-Ü]{1}[a-zà-ü']+\s[a-zA-Zà-üÀ-Ü]+((([\s\.'])|([a-zà-ü']+))|[a-zà-ü']+[a-zA-Zà-üÀ-Ü']+))
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"Aa "+"a"*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """(^[A-ZÀ-Ü]{1}[a-zà-ü']+\s[a-zA-Zà-üÀ-Ü]+((([\s\.'])|([a-zà-ü']+))|[a-zà-ü']+[a-zA-Zà-üÀ-Ü']+))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "Aa " + "a" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")