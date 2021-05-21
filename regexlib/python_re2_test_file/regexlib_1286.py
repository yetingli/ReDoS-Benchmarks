# 1286
# &lt;select(.|\n)*?selected(.|\n)*?&gt;(.*?)&lt;/option&gt;(.|\n)*?&lt;/select&gt;
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"&lt;selectselected&gt;"*128+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """&lt;select(.|\n)*?selected(.|\n)*?&gt;(.*?)&lt;/option&gt;(.|\n)*?&lt;/select&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;selectselected&gt;" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")