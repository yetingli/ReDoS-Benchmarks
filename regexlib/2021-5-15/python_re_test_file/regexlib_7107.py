# 7107
# &lt;[aA][ ]{0,}([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,}&gt;((&lt;(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})&gt;([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})|(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})){0,}
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"&lt;a"+" "*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """&lt;[aA][ ]{0,}([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,}&gt;((&lt;(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})&gt;([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})|(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})){0,}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&lt;a" + " " * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")