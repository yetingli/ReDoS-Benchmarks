# 3279
# href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\"
# EXPONENT
# nums:5
# EXPONENT AttackString:"href="/i/"+"1"*16+"! _1_NQ"

import re2 as re
from time import perf_counter

regex = """href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\""""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "href=\"/i/" + "1" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")