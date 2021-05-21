# 7879
# (?:(?:(\d+)[ ]*\'){0,1}[ ]*(\d*(?![/\w])){0,1}(?:[ ,\-]){0,1}(\d*\/\d*){0,1}(\.\d*){0,1}\")|(?:(\d+)[ ]*\'[ ]*){1}
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"1"*5000+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?:(?:(\d+)[ ]*\'){0,1}[ ]*(\d*(?![/\w])){0,1}(?:[ ,\-]){0,1}(\d*\/\d*){0,1}(\.\d*){0,1}\")|(?:(\d+)[ ]*\'[ ]*){1}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")