# 7889
# (?:(?:(?<=[\s^,(])\*(?=\S)(?!_)(?<bold>.+?)(?<!_)(?<=\S)\*(?=[\s$,.?!]))|(?:(?<=[\s^,(])_(?=\S)(?!\*)(?<underline>.+?)(?<!\*)(?<=\S)_(?=[\s$,.?!]))|(?:(?<=[\s^,(])(?:\*_|_\*)(?=\S)(?<boldunderline>.+?)(?<=\S)(?:\*_|_\*)(?=[\s$,.?!])))
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"<= *=!!_1<!_<=!*= <= _=!!*1<!*<=!_= "+"<= *_=!"*5000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?:(?:(?<=[\s^,(])\*(?=\S)(?!_)(?<bold>.+?)(?<!_)(?<=\S)\*(?=[\s$,.?!]))|(?:(?<=[\s^,(])_(?=\S)(?!\*)(?<underline>.+?)(?<!\*)(?<=\S)_(?=[\s$,.?!]))|(?:(?<=[\s^,(])(?:\*_|_\*)(?=\S)(?<boldunderline>.+?)(?<=\S)(?:\*_|_\*)(?=[\s$,.?!])))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<= *=!!_1<!_<=!*= <= _=!!*1<!*<=!_= " + "<= *_=!" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")