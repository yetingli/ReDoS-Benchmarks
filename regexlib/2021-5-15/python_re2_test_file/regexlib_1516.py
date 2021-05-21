# 1516
# ^(([A-Za-z]+[^0-9]*)([0-9]+[^\W]*)([\W]+[\W0-9A-Za-z]*))|(([A-Za-z]+[^\W]*)([\W]+[^0-9]*)([0-9]+[\W0-9A-Za-z]*))|(([\W]+[^A-Za-z]*)([A-Za-z]+[^0-9]*)([0-9]+[\W0-9A-Za-z]*))|(([\W]+[^0-9]*)([0-9]+[^A-Za-z]*)([A-Za-z]+[\W0-9A-Za-z]*))|(([0-9]+[^A-Za-z]*)([A-Za-z]+[^\W]*)([\W]+[\W0-9A-Za-z]*))|(([0-9]+[^\W]*)([\W]+[^A-Za-z]*)([A-Za-z]+[\W0-9A-Za-z]*))$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"AA0!"+"!"*5000+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(([A-Za-z]+[^0-9]*)([0-9]+[^\W]*)([\W]+[\W0-9A-Za-z]*))|(([A-Za-z]+[^\W]*)([\W]+[^0-9]*)([0-9]+[\W0-9A-Za-z]*))|(([\W]+[^A-Za-z]*)([A-Za-z]+[^0-9]*)([0-9]+[\W0-9A-Za-z]*))|(([\W]+[^0-9]*)([0-9]+[^A-Za-z]*)([A-Za-z]+[\W0-9A-Za-z]*))|(([0-9]+[^A-Za-z]*)([A-Za-z]+[^\W]*)([\W]+[\W0-9A-Za-z]*))|(([0-9]+[^\W]*)([\W]+[^A-Za-z]*)([A-Za-z]+[\W0-9A-Za-z]*))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "AA0!" + "!" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")