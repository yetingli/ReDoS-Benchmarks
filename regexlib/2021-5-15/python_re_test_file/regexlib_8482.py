# 8482
# ((MON|TUE|WED|THU|FRI|SAT|SUN)[A-Z]*)*[\ ,-]*(\d|\d{2})*(st|nd|rd|th)*[\ ,-]*(JAN|FEB|MAR|MAY|APR|JUL|JUN|AUG|OCT|SEP|NOV|DEC)[A-Z]*[\ ,]*(\d|\d{2}|\d{4})*(st|nd|rd|th)*([\ ,])*'*(\d{2}|\d{4})*\b
# EXPONENT
# nums:4
# EXPONENT AttackString:"JAN"+"00"*16+"! _1_EOD(i4)"

import re
from time import perf_counter

regex = """((MON|TUE|WED|THU|FRI|SAT|SUN)[A-Z]*)*[\ ,-]*(\d|\d{2})*(st|nd|rd|th)*[\ ,-]*(JAN|FEB|MAR|MAY|APR|JUL|JUN|AUG|OCT|SEP|NOV|DEC)[A-Z]*[\ ,]*(\d|\d{2}|\d{4})*(st|nd|rd|th)*([\ ,])*'*(\d{2}|\d{4})*\b"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "JAN" + "00" * i * 1 + "! _1_EOD(i4)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")