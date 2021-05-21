# 2358
# <img\s((width|height|alt|align|style)="[^"]*"\s)*src="(\/?[a-z0-9_-]\/?)+\.(png|jpg|jpeg|gif)"(\s(width|height|alt|align|style)="[^"]*")*\s*\/>
# EXPONENT
# nums:4
# EXPONENT AttackString:"<img src=""+"/-"*32+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """<img\s((width|height|alt|align|style)="[^"]*"\s)*src="(\/?[a-z0-9_-]\/?)+\.(png|jpg|jpeg|gif)"(\s(width|height|alt|align|style)="[^"]*")*\s*\/>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<img src=\"" + "/-" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")