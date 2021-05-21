# 7935
# (([\n,  ])*((<+)([^<>]+)(>*))+([\n,  ])*)+
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"\n< >\n"*16+"SLQ_1"

import re
from time import perf_counter

regex = """(([\n,  ])*((<+)([^<>]+)(>*))+([\n,  ])*)+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "\n< >\n" * i * 1 + "SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")