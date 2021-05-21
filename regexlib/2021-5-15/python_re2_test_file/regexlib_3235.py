# 3235
# <img[^>]*src=\"?([^\"]*)\"?([^>]*alt=\"?([^\"]*)\"?)?[^>]*>
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"<img"*5000+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """<img[^>]*src=\"?([^\"]*)\"?([^>]*alt=\"?([^\"]*)\"?)?[^>]*>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<img" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")