# 4184
# ((http|https|ftp|telnet|gopher|ms\-help|file|notes)://)?(([a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)(:.*)?@)?(([a-z0-9][\w\-]*[a-z0-9]*\.)*(((([a-z0-9][\w\-]*[a-z0-9]*)(\.[a-z0-9]+)?)|(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))(:[0-9]+)?))?(((/([\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(%\d\d))+)*/([\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(%\d\d))*)(\?[^#]+)?(#[a-z0-9]\w*)?)?
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"00."*32+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """((http|https|ftp|telnet|gopher|ms\-help|file|notes)://)?(([a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)(:.*)?@)?(([a-z0-9][\w\-]*[a-z0-9]*\.)*(((([a-z0-9][\w\-]*[a-z0-9]*)(\.[a-z0-9]+)?)|(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))(:[0-9]+)?))?(((/([\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(%\d\d))+)*/([\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(%\d\d))*)(\?[^#]+)?(#[a-z0-9]\w*)?)?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "00." * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")