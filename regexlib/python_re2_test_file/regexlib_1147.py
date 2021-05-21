# 1147
# (?<Element>((\*|\w+)?)) (?<Complement>((\.|\#|\-|\w|\:)*)) (?<FamilySeparator>([\s\>\+\~]|[\,\{]))
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:" "+"0"*10000+"! _1!1 _◎@! _1!\n_SLQ_3"

import re2 as re
from time import perf_counter

regex = """(?<Element>((\*|\w+)?)) (?<Complement>((\.|\#|\-|\w|\:)*)) (?<FamilySeparator>([\s\>\+\~]|[\,\{]))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = " " + "0" * i * 10000 + "! _1!1 _◎@! _1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")