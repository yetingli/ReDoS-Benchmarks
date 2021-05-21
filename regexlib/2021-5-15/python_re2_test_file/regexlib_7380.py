# 7380
# ((ht|f)tp(s?))(:((\/\/)(?!\/)))(((w){3}\.)?)([a-zA-Z0-9\-_]+(\.(com|edu|gov|int|mil|net|org|biz|info|name|pro|museum|co\.uk)))(\/(?!\/))(([a-zA-Z0-9\-_\/]*)?)([a-zA-Z0-9])+\.((jpg|jpeg|gif|png)(?!(\w|\W)))
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"http://a.com/"+"www"*5000+"! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """((ht|f)tp(s?))(:((\/\/)(?!\/)))(((w){3}\.)?)([a-zA-Z0-9\-_]+(\.(com|edu|gov|int|mil|net|org|biz|info|name|pro|museum|co\.uk)))(\/(?!\/))(([a-zA-Z0-9\-_\/]*)?)([a-zA-Z0-9])+\.((jpg|jpeg|gif|png)(?!(\w|\W)))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://a.com/" + "www" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")