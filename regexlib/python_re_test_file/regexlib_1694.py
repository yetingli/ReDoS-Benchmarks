# 1694
# ((A[FGIKLMNPRSUZ]S?X?|DAL?L?A?E?S?|DE|DE[LNRST]L?A?E?H?I?O?S?|DI[AE]?|DOS?|DU|EIT?N?E?|ELS?|EN|ETT?|HAI?|HE[NT]|HIN?A?I?N?R?|HOI|IL|IM|ISA|KA|KE|LAS|LES?|LH?IS?|LOS?|LO?U|MA?C|N[AIY]|O[IP]|SI|T[AEO]N?R?|U[MN][AEOS]?|VAN|VE[LR]|VO[MN]|Y[ENR]|ZU[MR]?) )?((LAS?|LOS?|DEN?R?|ZU) )?[A-Z0/'\.-]+( |$)(SR|JR|II+V?|VI+|[1-9][STRDH]+)?
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"II"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """((A[FGIKLMNPRSUZ]S?X?|DAL?L?A?E?S?|DE|DE[LNRST]L?A?E?H?I?O?S?|DI[AE]?|DOS?|DU|EIT?N?E?|ELS?|EN|ETT?|HAI?|HE[NT]|HIN?A?I?N?R?|HOI|IL|IM|ISA|KA|KE|LAS|LES?|LH?IS?|LOS?|LO?U|MA?C|N[AIY]|O[IP]|SI|T[AEO]N?R?|U[MN][AEOS]?|VAN|VE[LR]|VO[MN]|Y[ENR]|ZU[MR]?) )?((LAS?|LOS?|DEN?R?|ZU) )?[A-Z0/'\.-]+( |$)(SR|JR|II+V?|VI+|[1-9][STRDH]+)?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "II" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")