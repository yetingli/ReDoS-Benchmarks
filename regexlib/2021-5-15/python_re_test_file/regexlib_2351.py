# 2351
# &lt;a[\s]+[^&gt;]*?href[\s]?=[\s\&quot;\']+(.*?)[\&quot;\']+.*?&gt;([^&lt;]+|.*?)?&lt;\/a&gt;
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"&lt;a href= &"*128+"! _1SLQ_2"

import re
from time import perf_counter

regex = """&lt;a[\s]+[^&gt;]*?href[\s]?=[\s\&quot;\']+(.*?)[\&quot;\']+.*?&gt;([^&lt;]+|.*?)?&lt;\/a&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;a href= &" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")