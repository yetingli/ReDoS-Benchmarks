# 8347
# (?i)(?s)<a[^>]+?href="?(?<url>[^"]+)"?>(?<innerHtml>.+?)</a\s*>
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"is<a"*10000+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?i)(?s)<a[^>]+?href="?(?<url>[^"]+)"?>(?<innerHtml>.+?)</a\s*>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "is<a" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")