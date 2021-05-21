# 2075
# (?<LastName>[A-Z]\w+\-?[A-Z]?\w*),\s(?<Suffix>Jr\.|Sr\.|IV|III|II)?,?\s?(?<FirstName>[A-Z]\w*\-?[A-Z]?\w*\.?)\s?(?<MiddleName>[A-Z]?\w*\.?)
# EXPONENT
# nums:5
# EXPONENT AttackString:"A1, "+"A"*512+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?<LastName>[A-Z]\w+\-?[A-Z]?\w*),\s(?<Suffix>Jr\.|Sr\.|IV|III|II)?,?\s?(?<FirstName>[A-Z]\w*\-?[A-Z]?\w*\.?)\s?(?<MiddleName>[A-Z]?\w*\.?)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "A1, " + "A" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")