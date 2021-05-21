# 7091
# ^(([A-Za-z][A-Za-z0-9.+]*?){1,}?)(,\s?([^/\\:*?"<>|]*((,\s?(Version=(\d\.?){1,4}|Culture=(neutral|\w{2}-\w{2})|PublicKeyToken=[a-f0-9]{16})(,\s?)?){3}|))){0,1}$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"A"*32+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(([A-Za-z][A-Za-z0-9.+]*?){1,}?)(,\s?([^/\\:*?"<>|]*((,\s?(Version=(\d\.?){1,4}|Culture=(neutral|\w{2}-\w{2})|PublicKeyToken=[a-f0-9]{16})(,\s?)?){3}|))){0,1}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")