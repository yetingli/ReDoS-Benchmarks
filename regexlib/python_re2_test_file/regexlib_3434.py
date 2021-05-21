# 3434
# \d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\s.\s.\s\[\d{2}\/\D{3}\/\d{4}:\d{1,2}:\d{1,2}:\d{1,2}\s.\d{4}\]\s\&quot;\S*\s\S*\s\S*\&quot;\s\d{1,3}\s\S*\s\&quot;.*\&quot;\s\&quot;.*\&quot;
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"1.1.1.1 1 1 [11/:::/1111:1:1:1 11111] &quot;  &quot; 1  &quot;"*5000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\s.\s.\s\[\d{2}\/\D{3}\/\d{4}:\d{1,2}:\d{1,2}:\d{1,2}\s.\d{4}\]\s\&quot;\S*\s\S*\s\S*\&quot;\s\d{1,3}\s\S*\s\&quot;.*\&quot;\s\&quot;.*\&quot;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1.1.1.1 1 1 [11/:::/1111:1:1:1 11111] &quot;  &quot; 1  &quot;" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")