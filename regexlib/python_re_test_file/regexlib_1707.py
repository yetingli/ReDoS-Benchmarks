# 1707
# (<log4j:Event logger=")(.*?)(" timestamp=")(.*?)(" level=")(.*?)(" thread=")(.*?)(">)(.*?)(<log4j:Message><!\[CDATA\[)(.*?)(\]\]>)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"<log4j:Event logger="" timestamp="" level="" thread=""*64+"! _1SLQ_2"

import re
from time import perf_counter

regex = """(<log4j:Event logger=")(.*?)(" timestamp=")(.*?)(" level=")(.*?)(" thread=")(.*?)(">)(.*?)(<log4j:Message><!\[CDATA\[)(.*?)(\]\]>)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<log4j:Event logger=\"\" timestamp=\"\" level=\"\" thread=\"" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")