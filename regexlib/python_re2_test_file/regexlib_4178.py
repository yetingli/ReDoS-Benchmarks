# 4178
# ^(?:mailto:)?(?:[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)@(?:[a-z0-9][\w\-]*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9][\w\-]*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))$
# EXPONENT
# nums:5
# EXPONENT AttackString:"a@250.250.250."+"000"*256+"! _1_EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^(?:mailto:)?(?:[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)@(?:[a-z0-9][\w\-]*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9][\w\-]*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a@250.250.250." + "000" * i * 1 + "! _1_EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")