# 2766
# (?:@[A-Z]\w*\s+)*(?:(?:public|private|protected)\s+)?(?:(?:(?:abstract|final|native|transient|static|synchronized)\s+)*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>\s+)?(?:(?:(?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\]))*)|void)+)\s+(([a-zA-Z]\w*)\s*\(\s*(((?:[A-Z]\w*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>)?|int|float|double|char|boolean|byte|long|short)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*)(?:,\s*((?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*))*)?\s*\))
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"A"*32+"! _1_EOA(iii)"

import re2 as re
from time import perf_counter

regex = """(?:@[A-Z]\w*\s+)*(?:(?:public|private|protected)\s+)?(?:(?:(?:abstract|final|native|transient|static|synchronized)\s+)*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>\s+)?(?:(?:(?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\]))*)|void)+)\s+(([a-zA-Z]\w*)\s*\(\s*(((?:[A-Z]\w*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>)?|int|float|double|char|boolean|byte|long|short)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*)(?:,\s*((?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*))*)?\s*\))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 1 + "! _1_EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")