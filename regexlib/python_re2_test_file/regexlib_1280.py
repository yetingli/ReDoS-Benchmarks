# 1280
# (((0*[1-9]|[12][0-9]|3[01])([-./])(0*[13578]|10|12)([-./])(\d{4}))|((0*[1-9]|[12][0-9]|30)([-./])(0*[469]|11)([-./])(\d{4}))|((0*[1-9]|1[0-9]|2[0-8])([-./])(02|2)([-./])(\d{4}))|((29)(\.|-|\/)(02|2)([-./])([02468][048]00))|((29)([-./])(02|2)([-./])([13579][26]00))|((29)([-./])(02|2)([-./])([0-9][0-9][0][48]))|((29)([-./])(02|2)([-./])([0-9][0-9][2468][048]))|((29)([-./])(02|2)([-./])([0-9][0-9][13579][26])))
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"0"*10000+"!1 _!1 _SLQ_1"

import re2 as re
from time import perf_counter

regex = """(((0*[1-9]|[12][0-9]|3[01])([-./])(0*[13578]|10|12)([-./])(\d{4}))|((0*[1-9]|[12][0-9]|30)([-./])(0*[469]|11)([-./])(\d{4}))|((0*[1-9]|1[0-9]|2[0-8])([-./])(02|2)([-./])(\d{4}))|((29)(\.|-|\/)(02|2)([-./])([02468][048]00))|((29)([-./])(02|2)([-./])([13579][26]00))|((29)([-./])(02|2)([-./])([0-9][0-9][0][48]))|((29)([-./])(02|2)([-./])([0-9][0-9][2468][048]))|((29)([-./])(02|2)([-./])([0-9][0-9][13579][26])))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "!1 _!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")