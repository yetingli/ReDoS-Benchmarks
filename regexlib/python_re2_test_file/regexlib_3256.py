# 3256
# ^jdbc:db2://((?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?[.]))*)(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?)))):([0-9]{1,5})/([0-9|A-Z|a-z|_|#|$]{1,16})$
# EXPONENT
# nums:5
# EXPONENT AttackString:"jdbc:db2://"+"A0."*32+"! _1_EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^jdbc:db2://((?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?[.]))*)(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?)))):([0-9]{1,5})/([0-9|A-Z|a-z|_|#|$]{1,16})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "jdbc:db2://" + "A0." * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")