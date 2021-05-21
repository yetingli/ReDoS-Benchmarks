# 5284
# ((www|http)(\W+\S+[^).,:;?\]\} \r\n$]+))
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"www"+",,"*5000+"@1 _SLQ_2"

import re
from time import perf_counter

regex = """((www|http)(\W+\S+[^).,:;?\]\} \r\n$]+))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "www" + ",," * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")