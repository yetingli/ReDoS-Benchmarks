# 3613
# <(?<tag>\w*|\w*\.+\w*)>+((.|[\n\t\f\r\s])*?)<\/\k<tag>>
# EXPONENT
# nums:5
# EXPONENT AttackString:"<>"+"\t\t"*16+"! _1_EOD(i2)"

import re2 as re
from time import perf_counter

regex = """<(?<tag>\w*|\w*\.+\w*)>+((.|[\n\t\f\r\s])*?)<\/\k<tag>>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<>" + "\t\t" * i * 1 + "! _1_EOD(i2)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")