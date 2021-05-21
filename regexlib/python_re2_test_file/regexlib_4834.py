# 4834
# (http|ftp|https):\/\/(\w[\w\-_\.]*\.)?([_\-\w]+)(:[0-9]+)?([\/[\w_\.-]+]*)\/(\.?\w[\w._-]*[\w_-])?(#\w+)?([\w\-\.,@?^=%&amp;:\~\+#]*[\w\-\@?^=%&amp;\/\~\+#])?
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"http://"+"1"*10000+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """(http|ftp|https):\/\/(\w[\w\-_\.]*\.)?([_\-\w]+)(:[0-9]+)?([\/[\w_\.-]+]*)\/(\.?\w[\w._-]*[\w_-])?(#\w+)?([\w\-\.,@?^=%&amp;:\~\+#]*[\w\-\@?^=%&amp;\/\~\+#])?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://" + "1" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")