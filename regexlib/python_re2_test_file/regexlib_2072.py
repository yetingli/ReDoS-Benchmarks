# 2072
# (?<FirstName>[A-Z]\.?\w*\-?[A-Z]?\w*)\s?(?<MiddleName>[A-Z]\w*|[A-Z]?\.?)\s?(?<LastName>[A-Z]\w*\-?[A-Z]?\w*)(?:,\s|)(?<Suffix>Jr\.|Sr\.|IV|III|II|)
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"A"*64+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?<FirstName>[A-Z]\.?\w*\-?[A-Z]?\w*)\s?(?<MiddleName>[A-Z]\w*|[A-Z]?\.?)\s?(?<LastName>[A-Z]\w*\-?[A-Z]?\w*)(?:,\s|)(?<Suffix>Jr\.|Sr\.|IV|III|II|)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")