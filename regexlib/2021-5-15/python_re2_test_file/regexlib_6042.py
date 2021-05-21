# 6042
# (<\/?)(?i:(?<element>a(bbr|cronym|ddress|pplet|rea)?|b(ase(font)?|do|ig|lockquote|ody|r|utton)?|c(aption|enter|ite|(o(de|l(group)?)))|d(d|el|fn|i(r|v)|l|t)|em|f(ieldset|o(nt|rm)|rame(set)?)|h([1-6]|ead|r|tml)|i(frame|mg|n(put|s)|sindex)?|kbd|l(abel|egend|i(nk)?)|m(ap|e(nu|ta))|no(frames|script)|o(bject|l|pt(group|ion))|p(aram|re)?|q|s(amp|cript|elect|mall|pan|t(r(ike|ong)|yle)|u(b|p))|t(able|body|d|extarea|foot|h|itle|r|t)|u(l)?|var))(\s(?<attr>.+?))*>
# EXPONENT
# nums:5
# EXPONENT AttackString:"<a"+" "*32+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(<\/?)(?i:(?<element>a(bbr|cronym|ddress|pplet|rea)?|b(ase(font)?|do|ig|lockquote|ody|r|utton)?|c(aption|enter|ite|(o(de|l(group)?)))|d(d|el|fn|i(r|v)|l|t)|em|f(ieldset|o(nt|rm)|rame(set)?)|h([1-6]|ead|r|tml)|i(frame|mg|n(put|s)|sindex)?|kbd|l(abel|egend|i(nk)?)|m(ap|e(nu|ta))|no(frames|script)|o(bject|l|pt(group|ion))|p(aram|re)?|q|s(amp|cript|elect|mall|pan|t(r(ike|ong)|yle)|u(b|p))|t(able|body|d|extarea|foot|h|itle|r|t)|u(l)?|var))(\s(?<attr>.+?))*>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<a" + " " * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")