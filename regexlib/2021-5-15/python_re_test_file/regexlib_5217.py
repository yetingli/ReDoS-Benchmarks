# 5217
# ^(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}/(DC=['\w\d\s\-\&amp;]+[,]*){2,})|((\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])/(DC=['\w\d\s\-\&amp;]+[,]*){2,})|((DC=['\w\d\s\-\&amp;]+[,]*){2,})$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"DC=',DC=',"*5000+"! _1SLQ_1"

import re
from time import perf_counter

regex = """^(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}/(DC=['\w\d\s\-\&amp;]+[,]*){2,})|((\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])/(DC=['\w\d\s\-\&amp;]+[,]*){2,})|((DC=['\w\d\s\-\&amp;]+[,]*){2,})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "DC=\',DC=\'," * i * 10000 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")