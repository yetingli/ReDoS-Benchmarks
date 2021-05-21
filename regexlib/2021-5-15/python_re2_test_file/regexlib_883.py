# 883
# (?<expo>public\:|protected\:|private\:) (?<ret>(const )*(void|int|unsigned int|long|unsigned long|float|double|(class .*)|(enum .*))) (?<decl>__thiscall|__cdecl|__stdcall|__fastcall|__clrcall) (?<ns>.*)\:\:(?<class>(.*)((<.*>)*))\:\:(?<method>(.*)((<.*>)*))\((?<params>((.*(<.*>)?)(,)?)*)\)
# EXPONENT
# nums:5
# EXPONENT AttackString:"public: void __thiscall ::::("+"!"*16+"! _1_NQ"

import re2 as re
from time import perf_counter

regex = """(?<expo>public\:|protected\:|private\:) (?<ret>(const )*(void|int|unsigned int|long|unsigned long|float|double|(class .*)|(enum .*))) (?<decl>__thiscall|__cdecl|__stdcall|__fastcall|__clrcall) (?<ns>.*)\:\:(?<class>(.*)((<.*>)*))\:\:(?<method>(.*)((<.*>)*))\((?<params>((.*(<.*>)?)(,)?)*)\)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "public: void __thiscall ::::(" + "!" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")