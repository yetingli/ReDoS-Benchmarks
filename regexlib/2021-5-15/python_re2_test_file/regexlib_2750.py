# 2750
# ^(?<From>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9])+)(-|–|:|TO)?(?<To>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9]|PRESENT)+)+(:)*
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"JUNE "*16+"! _1_EOD(i2)"

import re2 as re
from time import perf_counter

regex = """^(?<From>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9])+)(-|–|:|TO)?(?<To>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9]|PRESENT)+)+(:)*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "JUNE " * i * 1 + "! _1_EOD(i2)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")