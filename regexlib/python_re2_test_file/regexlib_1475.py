# 1475
# (((ftp|http|https):\/\/)|(\w+:{0,1}\w*@))?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"0"*10000+"! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """(((ftp|http|https):\/\/)|(\w+:{0,1}\w*@))?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")