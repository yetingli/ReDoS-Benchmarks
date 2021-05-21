# 3303
# (\/\*[\s\S.]+?\*\/|[/]{2,}.*|\/((\\\/)|.??)*\/[gim]{0,3}|'((\\\')|.??)*'|"((\\\")|.??)*"|-?\d+\.\d+e?-?e?\d*|-?\.\d+e-?\d+|\w+|[\[\]\(\)\{\}:=;"'\-&!|+,.\/*])
# EXPONENT
# nums:4
# EXPONENT AttackString:"/"+"\\/"*32+"◎@! _1_EOD(i1)"

import re
from time import perf_counter

regex = """(\/\*[\s\S.]+?\*\/|[/]{2,}.*|\/((\\\/)|.??)*\/[gim]{0,3}|'((\\\')|.??)*'|"((\\\")|.??)*"|-?\d+\.\d+e?-?e?\d*|-?\.\d+e-?\d+|\w+|[\[\]\(\)\{\}:=;"'\-&!|+,.\/*])"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "/" + "\\/" * i * 1 + "◎@! _1_EOD(i1)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")