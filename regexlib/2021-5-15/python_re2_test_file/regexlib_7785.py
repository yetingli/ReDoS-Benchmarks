# 7785
# ^([A-Z]|[a-z]|[0-9])([A-Z]|[a-z]|[0-9]|([A-Z]|[a-z]|[0-9]|(%|&|'|\+|\-|@|_|\.|\ )[^%&'\+\-@_\.\ ]|\.$|([%&'\+\-@_\.]\ [^\ ]|\ [%&'\+\-@_\.][^%&'\+\-@_\.])))+$
# EXPONENT
# nums:5
# EXPONENT AttackString:"A"+"A0"*16+"!1 __EOD(i1)"

import re2 as re
from time import perf_counter

regex = """^([A-Z]|[a-z]|[0-9])([A-Z]|[a-z]|[0-9]|([A-Z]|[a-z]|[0-9]|(%|&|'|\+|\-|@|_|\.|\ )[^%&'\+\-@_\.\ ]|\.$|([%&'\+\-@_\.]\ [^\ ]|\ [%&'\+\-@_\.][^%&'\+\-@_\.])))+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "A" + "A0" * i * 1 + "!1 __EOD(i1)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")