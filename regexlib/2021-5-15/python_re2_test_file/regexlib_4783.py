# 4783
# (((?<numb1>[\d\.-]+)([\s]*?)(?<oper1>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)){0,1})(?<varname>(salary|mph|kph|ph){1})((([\s]*?)(?<oper2>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)(?<numb2>[\d\.-]+)){0,1})
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"1"*5000+"!1 _!1 _! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """(((?<numb1>[\d\.-]+)([\s]*?)(?<oper1>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)){0,1})(?<varname>(salary|mph|kph|ph){1})((([\s]*?)(?<oper2>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)(?<numb2>[\d\.-]+)){0,1})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "!1 _!1 _! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")