# 3436
# \(?\s*(?<area>\d{3})\s*[\)\.\-]?\s*(?<first>\d{3})\s*[\-\.]?\s*(?<second>\d{4})\D*(?<ext>\d*)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"111"+"\t"*10000+"◎@! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """\(?\s*(?<area>\d{3})\s*[\)\.\-]?\s*(?<first>\d{3})\s*[\-\.]?\s*(?<second>\d{4})\D*(?<ext>\d*)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "111" + "\t" * i * 10000 + "◎@! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")