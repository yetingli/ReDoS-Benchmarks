# 8543
# ^((([a-zA-Z\'\.\-]+)?)((,\s*([a-zA-Z]+))?)|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})))(;{1}(((([a-zA-Z\'\.\-]+){1})((,\s*([a-zA-Z]+))?))|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})){1}))*$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+";00000@00.AA"*8+"!1 __EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^((([a-zA-Z\'\.\-]+)?)((,\s*([a-zA-Z]+))?)|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})))(;{1}(((([a-zA-Z\'\.\-]+){1})((,\s*([a-zA-Z]+))?))|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})){1}))*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + ";00000@00.AA" * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")