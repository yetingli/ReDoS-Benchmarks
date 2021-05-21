# 1712
# (\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*(\s)*(\()(\s)*((int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*((\s)*[,](\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*)*)?(\s)*(\))(\s)*;
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"int"+"\t"*5000+"◎@! _1!_1!1 _!1 _!_1◎@! _1!_1! _1!_1◎@! _1!_1! _1!_1!\n_SLQ_3"

import re
from time import perf_counter

regex = """(\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*(\s)*(\()(\s)*((int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*((\s)*[,](\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*)*)?(\s)*(\))(\s)*;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "int" + "\t" * i * 10000 + "◎@! _1!_1!1 _!1 _!_1◎@! _1!_1! _1!_1◎@! _1!_1! _1!_1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")