# 1665
# (((ht|f)tp(s?):\/\/)(www\.[^ \[\]\(\)\n\r\t]+)|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})\/)([^ \[\]\(\),;&quot;\'&lt;&gt;\n\r\t]+)([^\. \[\]\(\),;&quot;\'&lt;&gt;\n\r\t])|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})
# EXPONENT
# nums:5
# EXPONENT AttackString:"http://"+"www."*1024+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """(((ht|f)tp(s?):\/\/)(www\.[^ \[\]\(\)\n\r\t]+)|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})\/)([^ \[\]\(\),;&quot;\'&lt;&gt;\n\r\t]+)([^\. \[\]\(\),;&quot;\'&lt;&gt;\n\r\t])|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://" + "www." * i * 1 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")