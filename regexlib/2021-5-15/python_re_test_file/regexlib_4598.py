# 4598
# ^([A-Z]+[a-zA-Z]*)(\s|\-)?([A-Z]+[a-zA-Z]*)?(\s|\-)?([A-Z]+[a-zA-Z]*)?$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"A"*64+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """^([A-Z]+[a-zA-Z]*)(\s|\-)?([A-Z]+[a-zA-Z]*)?(\s|\-)?([A-Z]+[a-zA-Z]*)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")