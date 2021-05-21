# 1550
# ((?!(This|It|He|She|[MTWFS][a-z]+day|[JF][a-z]+ary|March|April|May|June|July|August|[SOND][a-z]+ber))(?:[A-Z]+\.\s?)*(?:(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+)(?:(\b\s?((?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+|[A-Z]+\.|on|of|the|von|der|van|de|bin|and))*(?:\s*(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+))?)
# EXPONENT
# nums:4
# EXPONENT AttackString:"Aa"+"AA"*128+"! _1_EOA(iii)"

import re
from time import perf_counter

regex = """((?!(This|It|He|She|[MTWFS][a-z]+day|[JF][a-z]+ary|March|April|May|June|July|August|[SOND][a-z]+ber))(?:[A-Z]+\.\s?)*(?:(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+)(?:(\b\s?((?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+|[A-Z]+\.|on|of|the|von|der|van|de|bin|and))*(?:\s*(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+))?)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "Aa" + "AA" * i * 1 + "! _1_EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")