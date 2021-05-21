# 5490
# (LOC[^']*')(GID[^']*')?(GDS[^']*')?(FTX[^']*'){0,9}(MEA[^']*'){1,9}(DIM[^']*'){0,9}(TMP[^']*')?(RNG[^']*')?(LOC[^']*'){0,9}(RFF[^']*')((EQD[^']*')(EQA[^']*'){0,9}(NAD[^']*')?){0,3}
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"LOC"*10000+"@1 _SLQ_2"

import re
from time import perf_counter

regex = """(LOC[^']*')(GID[^']*')?(GDS[^']*')?(FTX[^']*'){0,9}(MEA[^']*'){1,9}(DIM[^']*'){0,9}(TMP[^']*')?(RNG[^']*')?(LOC[^']*'){0,9}(RFF[^']*')((EQD[^']*')(EQA[^']*'){0,9}(NAD[^']*')?){0,3}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "LOC" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")