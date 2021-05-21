# 7923
# &lt;asp:requiredfieldvalidator(\s*\w+\s*=\s*\&quot;?\s*\w+\s*\&quot;?\s*)+\s*&gt;\s*&lt;\/asp:requiredfieldvalidator&gt;
# EXPONENT
# nums:4
# EXPONENT AttackString:"&lt;asp:requiredfieldvalidator"+"\t0=&quot0&quot"*32+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """&lt;asp:requiredfieldvalidator(\s*\w+\s*=\s*\&quot;?\s*\w+\s*\&quot;?\s*)+\s*&gt;\s*&lt;\/asp:requiredfieldvalidator&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&lt;asp:requiredfieldvalidator" + "\t0=&quot0&quot" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")