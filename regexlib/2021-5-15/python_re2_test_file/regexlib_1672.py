# 1672
# \s*([a-z\. ]+)\s*\n\s*([a-z0-9\. #]+)\s*\n\s*([a-z \.]+)\s*,\s*([a-z \.]+)\s*\n?(?:\s*(\d{1,15}(?:-\d{1,4})?)\s*\n)?(?:\s*(\+?(?:1\s*[-\/\.]?)?(?:\((?:\d{3})\)|(?:\d{3}))\s*[-\/\.]?\s*(?:\d{3})\s*[-\/\.]?\s*(?:\d{4})(?:(?:[ \t]*[xX]|[eE][xX][tT])\.?[ \t]*(?:\d+))*))?
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"a"*10000+"!_1SLQ_2"

import re2 as re
from time import perf_counter

regex = """\s*([a-z\. ]+)\s*\n\s*([a-z0-9\. #]+)\s*\n\s*([a-z \.]+)\s*,\s*([a-z \.]+)\s*\n?(?:\s*(\d{1,15}(?:-\d{1,4})?)\s*\n)?(?:\s*(\+?(?:1\s*[-\/\.]?)?(?:\((?:\d{3})\)|(?:\d{3}))\s*[-\/\.]?\s*(?:\d{3})\s*[-\/\.]?\s*(?:\d{4})(?:(?:[ \t]*[xX]|[eE][xX][tT])\.?[ \t]*(?:\d+))*))?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")