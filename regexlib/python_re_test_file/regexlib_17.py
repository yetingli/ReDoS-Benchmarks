# 17
# (?s)( class=\w+(?=([^&lt;]*&gt;)))|(&lt;!--\[if.*?&lt;!\[endif\]--&gt;)|(&lt;!\[if !\w+\]&gt;)|(&lt;!\[endif\]&gt;)|(&lt;o:p&gt;[^&lt;]*&lt;/o:p&gt;)|(&lt;span[^&gt;]*&gt;)|(&lt;/span&gt;)|(font-family:[^&gt;]*[;'])|(font-size:[^&gt;]*[;'])(?-s)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:" class="+"0"*10000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """(?s)( class=\w+(?=([^&lt;]*&gt;)))|(&lt;!--\[if.*?&lt;!\[endif\]--&gt;)|(&lt;!\[if !\w+\]&gt;)|(&lt;!\[endif\]&gt;)|(&lt;o:p&gt;[^&lt;]*&lt;/o:p&gt;)|(&lt;span[^&gt;]*&gt;)|(&lt;/span&gt;)|(font-family:[^&gt;]*[;'])|(font-size:[^&gt;]*[;'])(?-s)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = " class=" + "0" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")