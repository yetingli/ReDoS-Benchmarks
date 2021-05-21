# 8244
# ^.*[_A-Za-z0-9]+[\t ]+[\*&]?[\t ]*[_A-Za-z0-9](::)?[_A-Za-z0-9:]+[\t ]*\(( *[ \[\]\*&A-Za-z0-9_]+ *,? *)*\).*$
# EXPONENT
# nums:4
# EXPONENT AttackString:"_\t__("+" "*16+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^.*[_A-Za-z0-9]+[\t ]+[\*&]?[\t ]*[_A-Za-z0-9](::)?[_A-Za-z0-9:]+[\t ]*\(( *[ \[\]\*&A-Za-z0-9_]+ *,? *)*\).*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "_\t__(" + " " * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")