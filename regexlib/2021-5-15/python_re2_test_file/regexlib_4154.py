# 4154
# ^(?<link>((?<prot>http:\/\/)*(?<subdomain>(www|[^\-\n]*)*)(\.)*(?<domain>[^\-\n]+)\.(?<after>[a-zA-Z]{2,3}[^>\n]*)))$
# EXPONENT
# nums:5
# EXPONENT AttackString:":."+"aa"*8+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(?<link>((?<prot>http:\/\/)*(?<subdomain>(www|[^\-\n]*)*)(\.)*(?<domain>[^\-\n]+)\.(?<after>[a-zA-Z]{2,3}[^>\n]*)))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = ":." + "aa" * i * 1 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")