# 8048
# ^(http(s?):\/\/)(www.)?(\w|-)+(\.(\w|-)+)*((\.[a-zA-Z]{2,3})|\.(aero|coop|info|museum|name))+(\/)?$
# EXPONENT
# nums:5
# EXPONENT AttackString:"http://1"+".aero.AA"*1024+"! _1_EOD(i2)"

import re2 as re
from time import perf_counter

regex = """^(http(s?):\/\/)(www.)?(\w|-)+(\.(\w|-)+)*((\.[a-zA-Z]{2,3})|\.(aero|coop|info|museum|name))+(\/)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://1" + ".aero.AA" * i * 1 + "! _1_EOD(i2)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")