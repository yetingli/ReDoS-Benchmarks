# 119
#  <\/{0,1}(?!\/|b>|i>|p>|a\s|a>|br|em>|ol|li|strong>)[^>]*>
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+" <!/"*10000+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """ <\/{0,1}(?!\/|b>|i>|p>|a\s|a>|br|em>|ol|li|strong>)[^>]*>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + " <!/" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")