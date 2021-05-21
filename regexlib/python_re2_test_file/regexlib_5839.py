# 5839
# &lt;(?:[^&quot;']+?|.+?(?:&quot;|').*?(?:&quot;|')?.*?)*?&gt;
# EXPONENT
# nums:5
# EXPONENT AttackString:"&lt;"+"'"*2+"! _1! _1! _1! _1! _1!\n_SLQ_3"

import re2 as re
from time import perf_counter

regex = """&lt;(?:[^&quot;']+?|.+?(?:&quot;|').*?(?:&quot;|')?.*?)*?&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&lt;" + "\'" * i * 1 + "! _1! _1! _1! _1! _1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")