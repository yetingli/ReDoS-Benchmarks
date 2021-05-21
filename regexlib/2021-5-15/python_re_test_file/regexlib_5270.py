# 5270
# ^[-]?P(?!$)(?:(?<year>\d+)+Y)?(?:(?<month>\d+)+M)?(?:(?<days>\d+)+D)?(?:T(?!$)(?:(?<hours>\d+)+H)?(?:(?<minutes>\d+)+M)? (?:(?<seconds>\d+(?:\.\d+)?)+S)?)?$
# EXPONENT
# nums:4
# EXPONENT AttackString:"PT "+"0"*32+"!1 __NQ"

import re
from time import perf_counter

regex = """^[-]?P(?!$)(?:(?<year>\d+)+Y)?(?:(?<month>\d+)+M)?(?:(?<days>\d+)+D)?(?:T(?!$)(?:(?<hours>\d+)+H)?(?:(?<minutes>\d+)+M)? (?:(?<seconds>\d+(?:\.\d+)?)+S)?)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "PT " + "0" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")