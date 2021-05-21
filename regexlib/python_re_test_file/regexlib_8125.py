# 8125
# <a.*? href=["|'].*\?(?<query>.*?)["|'].*?>
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"<a href="?"*64+"! _1SLQ_2"

import re
from time import perf_counter

regex = """<a.*? href=["|'].*\?(?<query>.*?)["|'].*?>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<a href=\"?" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")