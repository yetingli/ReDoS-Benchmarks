# 8038
# ^(http\://){1}(((www\.){1}([a-zA-Z0-9\-]*\.){1,}){1}|([a-zA-Z0-9\-]*\.){1,10}){1}([a-zA-Z]{2,6}\.){1}([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*
# EXPONENT
# nums:5
# EXPONENT AttackString:"http://www.."+"www.www.."*1024+"! _1_EOD(i2)"

import re2 as re
from time import perf_counter

regex = """^(http\://){1}(((www\.){1}([a-zA-Z0-9\-]*\.){1,}){1}|([a-zA-Z0-9\-]*\.){1,10}){1}([a-zA-Z]{2,6}\.){1}([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://www.." + "www.www.." * i * 1 + "! _1_EOD(i2)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")