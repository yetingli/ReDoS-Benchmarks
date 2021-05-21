# 7924
# \b((([&quot;'/,&amp;%\:\(\)\$\+\-\*\w\000-\032])|(-*\d+\.\d+[%]*))+[\s]+)+\b[\w&quot;',%\(\)]+[.!?](['&quot;\s]|$)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"&"+"1.1"*5000+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """\b((([&quot;'/,&amp;%\:\(\)\$\+\-\*\w\000-\032])|(-*\d+\.\d+[%]*))+[\s]+)+\b[\w&quot;',%\(\)]+[.!?](['&quot;\s]|$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&" + "1.1" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")