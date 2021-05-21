# 8179
# <a.*?href=[""'](?<uri>(?<path>.*?)file:(?<file>.*?))[""'].*?>(?<description>.*?)</a>
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"<ahref="file:">"*32+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """<a.*?href=[""'](?<uri>(?<path>.*?)file:(?<file>.*?))[""'].*?>(?<description>.*?)</a>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<ahref=\"file:\">" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")