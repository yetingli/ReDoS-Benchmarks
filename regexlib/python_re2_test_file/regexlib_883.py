# 883
# (?<expo>public\:|protected\:|private\:) (?<ret>(const )*(void|int|unsigned int|long|unsigned long|float|double|(class .*)|(enum .*))) (?<decl>__thiscall|__cdecl|__stdcall|__fastcall|__clrcall) (?<ns>.*)\:\:(?<class>(.*)((<.*>)*))\:\:(?<method>(.*)((<.*>)*))\((?<params>((.*(<.*>)?)(,)?)*)\)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"public: void __thiscall "*5000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?<expo>public\:|protected\:|private\:) (?<ret>(const )*(void|int|unsigned int|long|unsigned long|float|double|(class .*)|(enum .*))) (?<decl>__thiscall|__cdecl|__stdcall|__fastcall|__clrcall) (?<ns>.*)\:\:(?<class>(.*)((<.*>)*))\:\:(?<method>(.*)((<.*>)*))\((?<params>((.*(<.*>)?)(,)?)*)\)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "public: void __thiscall " * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")