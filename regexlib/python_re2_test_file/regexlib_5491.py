# 5491
# ((EQD[^']*')(RFF[^']*'){0,9}(EQN[^']*')?(TMD[^']*'){0,9}(DTM[^']*'){0,9}(LOC[^']*'){0,9}(MEA[^']*'){0,9}(DIM[^']*'){0,9}(TMP[^']*'){0,9}(RNG[^']*'){0,9}(SEL[^']*'){0,9}(FTX[^']*'){0,9}(DGS[^']*'){0,9}(EQA[^']*'){0,9}(NAD[^']*')?)((TDT[^']*')(RFF[^']*'){0,9}(LOC[^']*'){0,9}(DTM[^']*'){0,9})?
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"EQD"*10000+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """((EQD[^']*')(RFF[^']*'){0,9}(EQN[^']*')?(TMD[^']*'){0,9}(DTM[^']*'){0,9}(LOC[^']*'){0,9}(MEA[^']*'){0,9}(DIM[^']*'){0,9}(TMP[^']*'){0,9}(RNG[^']*'){0,9}(SEL[^']*'){0,9}(FTX[^']*'){0,9}(DGS[^']*'){0,9}(EQA[^']*'){0,9}(NAD[^']*')?)((TDT[^']*')(RFF[^']*'){0,9}(LOC[^']*'){0,9}(DTM[^']*'){0,9})?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "EQD" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")