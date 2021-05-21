# 3471
# \[bible[=]?([a-zäëïöüæø]*)\]((([0-9][[:space:]]?)?[a-zäëïöüæø]*[[:space:]]{1}([a-zäëïöüæø]*[[:space:]]?[a-zäëïöüæø]*[[:space:]]{1})?)([0-9]{1,3})(:{1}([0-9]{1,3})(-{1}([0-9]{1,3}))?)?)\[\\/bible\]
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"[bible]"+"a"*5000+"◎@! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """\[bible[=]?([a-zäëïöüæø]*)\]((([0-9][[:space:]]?)?[a-zäëïöüæø]*[[:space:]]{1}([a-zäëïöüæø]*[[:space:]]?[a-zäëïöüæø]*[[:space:]]{1})?)([0-9]{1,3})(:{1}([0-9]{1,3})(-{1}([0-9]{1,3}))?)?)\[\\/bible\]"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "[bible]" + "a" * i * 10000 + "◎@! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")