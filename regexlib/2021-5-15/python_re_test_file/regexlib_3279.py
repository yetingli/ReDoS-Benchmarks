# 3279
# href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\"
# EXPONENT
# nums:4
# EXPONENT AttackString:"href="/i/"+"%%"*8+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\""""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "href=\"/i/" + "%%" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")