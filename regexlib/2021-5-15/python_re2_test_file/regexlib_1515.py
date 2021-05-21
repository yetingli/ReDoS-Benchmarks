# 1515
# ^(http(s?)\:\/\/)*[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
# EXPONENT
# nums:5
# EXPONENT AttackString:"0"+"0"*32+"! _1_EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^(http(s?)\:\/\/)*[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "0" + "0" * i * 1 + "! _1_EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")