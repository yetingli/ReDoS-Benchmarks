# 225
# (<[^>]*?tag[^>]*?(?:identify_by)[^>]*>)((?:.*?(?:<[ \r\t]*tag[^>]*>?.*?(?:<.*?/.*?tag.*?>)?)*)*)(<[^>]*?/[^>]*?tag[^>]*?>)
# EXPONENT
# nums:5
# EXPONENT AttackString:"<tagidentify_by>"+"<tag</!tag</>"*2+"! _1_EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """(<[^>]*?tag[^>]*?(?:identify_by)[^>]*>)((?:.*?(?:<[ \r\t]*tag[^>]*>?.*?(?:<.*?/.*?tag.*?>)?)*)*)(<[^>]*?/[^>]*?tag[^>]*?>)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<tagidentify_by>" + "<tag</!tag</>" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")