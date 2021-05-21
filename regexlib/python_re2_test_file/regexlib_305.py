# 305
# (?<=(?:\n|:|^)\s*?)(if|end\sif|elseif|else|for\seach|for|next|call|class|exit|do|loop|const|dim|erase|option\s(?:explicit|implicit)|(?:public|private|end)\ssub|(?:public|private|end)\sfunction|private|public|redim|select\scase|end\sselect|case\selse|case|set|while|wend|with|end\swith|on\serror\sgoto\s0|on\serror\sresume\snext|exit|end\sclass|property\slet|property\sget|property\sset)(?=\s|$)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"<="+"\n"*5000+"!_1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?<=(?:\n|:|^)\s*?)(if|end\sif|elseif|else|for\seach|for|next|call|class|exit|do|loop|const|dim|erase|option\s(?:explicit|implicit)|(?:public|private|end)\ssub|(?:public|private|end)\sfunction|private|public|redim|select\scase|end\sselect|case\selse|case|set|while|wend|with|end\swith|on\serror\sgoto\s0|on\serror\sresume\snext|exit|end\sclass|property\slet|property\sget|property\sset)(?=\s|$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<=" + "\n" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")