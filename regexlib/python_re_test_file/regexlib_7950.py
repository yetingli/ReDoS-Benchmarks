# 7950
# ^((unit|u|)\s*)?(?<unit>\d*\w?)?(\s+|/)?(?<streetNo>\d+(\-\d+)?)\s+(?<streetName>\w+)\s+(?<streetType>\w+)\s+(?<suburb>\w+(\s+\w+)?)\s+(?<state>\w+)\s+(?<postcode>\d{4})$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"1"*5000+"!_1SLQ_2"

import re
from time import perf_counter

regex = """^((unit|u|)\s*)?(?<unit>\d*\w?)?(\s+|/)?(?<streetNo>\d+(\-\d+)?)\s+(?<streetName>\w+)\s+(?<streetType>\w+)\s+(?<suburb>\w+(\s+\w+)?)\s+(?<state>\w+)\s+(?<postcode>\d{4})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")