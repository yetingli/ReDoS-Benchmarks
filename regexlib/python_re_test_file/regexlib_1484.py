# 1484
# <a[a-zA-Z0-9 ="'.:;?]*(href=[\"\'](http:\/\/|\.\/|\/)?\w+(\.\w+)*(\/\w+(\.\w+)?)*(\/|\?\w*=\w*(&\w*=\w*)*)?[\"\'])*(>[a-zA-Z0-9 ="'<>.:;?]*</a>)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"<a"+"href="0""*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """<a[a-zA-Z0-9 ="'.:;?]*(href=[\"\'](http:\/\/|\.\/|\/)?\w+(\.\w+)*(\/\w+(\.\w+)?)*(\/|\?\w*=\w*(&\w*=\w*)*)?[\"\'])*(>[a-zA-Z0-9 ="'<>.:;?]*</a>)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<a" + "href=\"0\"" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")