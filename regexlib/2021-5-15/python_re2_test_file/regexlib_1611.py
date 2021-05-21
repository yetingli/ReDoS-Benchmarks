# 1611
# ^(((h|H)(t|T))(t|T)(p|P)((s|S)?)\:\/\/)?((www|WWW)+\.)+(([0-9]{1,3}){3}[0-9]{1,3}\.|([\w!~*'()-]+\.)*([\w^-][\w-]{0,61})?[\w]\.[a-z]{2,6})(:[0-9]{1,4})?((\/*)|(\/+[\w!~*'().;?:@&=+$,%#-]+)+\/*)$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"WWW."*5000+"! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """^(((h|H)(t|T))(t|T)(p|P)((s|S)?)\:\/\/)?((www|WWW)+\.)+(([0-9]{1,3}){3}[0-9]{1,3}\.|([\w!~*'()-]+\.)*([\w^-][\w-]{0,61})?[\w]\.[a-z]{2,6})(:[0-9]{1,4})?((\/*)|(\/+[\w!~*'().;?:@&=+$,%#-]+)+\/*)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "WWW." * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")