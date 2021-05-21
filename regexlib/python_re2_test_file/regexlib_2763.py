# 2763
# [0-9]+[stndrh]*\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*([0-9][0-9][0-9][0-9])?|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*[0-9]+[stndrh]*|[0-9]+[\/.-][0-9]+[\/.-][0-9]+[0-9]+|[saturnmoewdhfi]*day
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"s"*20000+"! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """[0-9]+[stndrh]*\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*([0-9][0-9][0-9][0-9])?|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*[0-9]+[stndrh]*|[0-9]+[\/.-][0-9]+[\/.-][0-9]+[0-9]+|[saturnmoewdhfi]*day"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "s" * i * 10000 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")