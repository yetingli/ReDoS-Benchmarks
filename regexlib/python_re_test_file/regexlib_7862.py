# 7862
# Password=(?<Password>.*);.*=(?<Info>.*);.*=(?<User>.*);.*=(?<Catalog>.*);.*=(?<Data>.*)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"Password="*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """Password=(?<Password>.*);.*=(?<Info>.*);.*=(?<User>.*);.*=(?<Catalog>.*);.*=(?<Data>.*)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "Password=" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")