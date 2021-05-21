# 7210
# ^[-\w'+*$^&%=~!?{}#|/`]{1}([-\w'+*$^&%=~!?{}#|`.]?[-\w'+*$^&%=~!?{}#|`]{1}){0,31}[-\w'+*$^&%=~!?{}#|`]?@(([a-zA-Z0-9]{1}([-a-zA-Z0-9]?[a-zA-Z0-9]{1}){0,31})\.{1})+([a-zA-Z]{2}|[a-zA-Z]{3}|[a-zA-Z]{4}|[a-zA-Z]{6}){1}$
# EXPONENT
# nums:5
# EXPONENT AttackString:"-@"+"0"*32+"@1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^[-\w'+*$^&%=~!?{}#|/`]{1}([-\w'+*$^&%=~!?{}#|`.]?[-\w'+*$^&%=~!?{}#|`]{1}){0,31}[-\w'+*$^&%=~!?{}#|`]?@(([a-zA-Z0-9]{1}([-a-zA-Z0-9]?[a-zA-Z0-9]{1}){0,31})\.{1})+([a-zA-Z]{2}|[a-zA-Z]{3}|[a-zA-Z]{4}|[a-zA-Z]{6}){1}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "-@" + "0" * i * 1 + "@1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")