# 1285
# &lt;input[^&gt;]*?type[/s]*=[/s]*(['|&quot;]?)text\1[^&gt;]*?value[/s]*=[/s]*(['|&quot;])(.*?)\2[^&gt;]*?&gt;
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"&lt;inputtype=textvalue='"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """&lt;input[^&gt;]*?type[/s]*=[/s]*(['|&quot;]?)text\1[^&gt;]*?value[/s]*=[/s]*(['|&quot;])(.*?)\2[^&gt;]*?&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;inputtype=textvalue=\'" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")