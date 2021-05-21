# 3817
# ^(https?|ftp)(:\/\/)(([\w]{3,}\.[\w]+\.[\w]{2,6})|([\d]{3}\.[\d]{1,3}\.[\d]{3}\.[\d]{1,3}))(\:[0,9]+)*(\/?$|((\/[\w\W]+)+\.[\w]{3,4})?$)
# EXPONENT
# nums:5
# EXPONENT AttackString:"http://111.1.11"+"/"*32+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(https?|ftp)(:\/\/)(([\w]{3,}\.[\w]+\.[\w]{2,6})|([\d]{3}\.[\d]{1,3}\.[\d]{3}\.[\d]{1,3}))(\:[0,9]+)*(\/?$|((\/[\w\W]+)+\.[\w]{3,4})?$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://111.1.11" + "/" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")