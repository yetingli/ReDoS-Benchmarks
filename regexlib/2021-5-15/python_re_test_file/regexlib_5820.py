# 5820
# (< *balise[ *>|:(.|\n)*>| (.|\n)*>](.|\n)*</balise *>)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"<balise </balise"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """(< *balise[ *>|:(.|\n)*>| (.|\n)*>](.|\n)*</balise *>)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<balise </balise" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")