# 6839
# <ul>\n<li>(?<type>document_name|url)=(?<doc>.*?)<li>.*?<ul>\n(?:<li>(?<propName>.*?)\n<li>(?<propValue>.*?))+</ul>\n</ul>
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"<ul>\n<li>document_name=<li>"*5000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """<ul>\n<li>(?<type>document_name|url)=(?<doc>.*?)<li>.*?<ul>\n(?:<li>(?<propName>.*?)\n<li>(?<propValue>.*?))+</ul>\n</ul>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<ul>\n<li>document_name=<li>" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")