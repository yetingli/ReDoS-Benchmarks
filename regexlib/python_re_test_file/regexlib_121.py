# 121
# <a\s{1}href="(?<url>.*?)"(\s?target="(?<target>_(blank|new|parent|self|top))")?(\s?class="(?<class>.*?)")?(\s?style="(?<style>.*?)")?>(?<title>.*?)</a>
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"<a href="""+"class=""*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """<a\s{1}href="(?<url>.*?)"(\s?target="(?<target>_(blank|new|parent|self|top))")?(\s?class="(?<class>.*?)")?(\s?style="(?<style>.*?)")?>(?<title>.*?)</a>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<a href=\"\"" + "class=\"" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")