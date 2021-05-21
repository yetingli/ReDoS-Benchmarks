# 2751
# (([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)([ ]|[:]|\t|[-])*(Home|Office|Work|Away|Fax|FAX|Phone)|(Home|Office|Work|Away|Fax|FAX|Phone|Daytime|Evening)([ ]|[:]|\t|[-])*(([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)|(([(]([0-9]){3}[)]([ ])?([0-9]){3}([ ]|-)([0-9]){4}))
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"0"*5000+"!1 _SLQ_1"

import re2 as re
from time import perf_counter

regex = """(([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)([ ]|[:]|\t|[-])*(Home|Office|Work|Away|Fax|FAX|Phone)|(Home|Office|Work|Away|Fax|FAX|Phone|Daytime|Evening)([ ]|[:]|\t|[-])*(([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)|(([(]([0-9]){3}[)]([ ])?([0-9]){3}([ ]|-)([0-9]){4}))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")