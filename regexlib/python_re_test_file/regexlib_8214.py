# 8214
# <(\s*/?\s*)\w+?(\s*(([\w-]+="[^"]*?")|([\w-]+='[^']*?')|([\w-]+=[^'"<>\s]+)))*(\s*/?\s*)>
# EXPONENT
# nums:4
# EXPONENT AttackString:"1=""1=''<1"+"1="*32+"@1 _SLQ_2"

import re
from time import perf_counter

regex = """<(\s*/?\s*)\w+?(\s*(([\w-]+="[^"]*?")|([\w-]+='[^']*?')|([\w-]+=[^'"<>\s]+)))*(\s*/?\s*)>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1=\"\"1=\'\'<1" + "1=" * i * 1 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")