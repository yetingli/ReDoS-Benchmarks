# 5504
# megaupload\.com.*(?:\?|&)(?:(?:folderi)?d|f)=([A-Z-a-z0-9]{8})
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"megaupload.com"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """megaupload\.com.*(?:\?|&)(?:(?:folderi)?d|f)=([A-Z-a-z0-9]{8})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "megaupload.com" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")