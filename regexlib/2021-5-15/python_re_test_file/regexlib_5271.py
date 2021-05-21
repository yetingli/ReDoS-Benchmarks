# 5271
# (\s*\S*){2}(ipsum)(\S*\s*){2}
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"\t"*512+"!_1_NQ"

import re
from time import perf_counter

regex = """(\s*\S*){2}(ipsum)(\S*\s*){2}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "\t" * i * 1 + "!_1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")