# 2353
# (((ht|f)tp(s?):\/\/)|(([\w]{1,})\.[^ \[\]\(\)\n\r\t]+)|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})\/)([^ \[\]\(\),;"'<>\n\r\t]+)([^\. \[\]\(\),;"'<>\n\r\t])|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"00.00.00."*512+"!1 _◎@! _1@1 _SLQ_1"

import re2 as re
from time import perf_counter

regex = """(((ht|f)tp(s?):\/\/)|(([\w]{1,})\.[^ \[\]\(\)\n\r\t]+)|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})\/)([^ \[\]\(\),;"'<>\n\r\t]+)([^\. \[\]\(\),;"'<>\n\r\t])|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "00.00.00." * i * 1 + "!1 _◎@! _1@1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")