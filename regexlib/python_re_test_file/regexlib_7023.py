# 7023
# ^(ht|f)tp(s?)\:\/\/[a-zA-Z0-9\-\._]+(\.[a-zA-Z0-9\-\._]+){2,}(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
# EXPONENT
# nums:4
# EXPONENT AttackString:"http://a.a.a"+"."*32+"! _1_EOA(iv)"

import re
from time import perf_counter

regex = """^(ht|f)tp(s?)\:\/\/[a-zA-Z0-9\-\._]+(\.[a-zA-Z0-9\-\._]+){2,}(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://a.a.a" + "." * i * 1 + "! _1_EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")