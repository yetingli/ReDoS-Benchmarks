# 2073
# (?<FirstName>[A-Z]\.?\w*\-?[A-Z]?\w*)\s?(?<MiddleName>[A-Z]\w+|[A-Z]?\.?)\s(?<LastName>[A-Z]?\w{0,3}[A-Z]\w+\-?[A-Z]?\w*)(?:,\s|)(?<Suffix>Jr\.|Sr\.|IV|III|II|)
# EXPONENT
# nums:5
# EXPONENT AttackString:"AA1 "+"A1"*512+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?<FirstName>[A-Z]\.?\w*\-?[A-Z]?\w*)\s?(?<MiddleName>[A-Z]\w+|[A-Z]?\.?)\s(?<LastName>[A-Z]?\w{0,3}[A-Z]\w+\-?[A-Z]?\w*)(?:,\s|)(?<Suffix>Jr\.|Sr\.|IV|III|II|)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "AA1 " + "A1" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")