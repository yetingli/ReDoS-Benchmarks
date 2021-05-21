# 7924
# \b((([&quot;'/,&amp;%\:\(\)\$\+\-\*\w\000-\032])|(-*\d+\.\d+[%]*))+[\s]+)+\b[\w&quot;',%\(\)]+[.!?](['&quot;\s]|$)
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"00.0"*16+"@1 __EOD(i3)"

import re2 as re
from time import perf_counter

regex = """\b((([&quot;'/,&amp;%\:\(\)\$\+\-\*\w\000-\032])|(-*\d+\.\d+[%]*))+[\s]+)+\b[\w&quot;',%\(\)]+[.!?](['&quot;\s]|$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "00.0" * i * 1 + "@1 __EOD(i3)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")