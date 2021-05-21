# 7093
# ^(?<Namespace>(?:[\w][\w\d]*\.?)*)\.(?<Class>[\w][\w\d<>]*(?:(?:\+[\w][\w\d<>]*)+|))(?:|,\W?(?<Assembly>(?<AssemblyName>[^\W/\\:*?"<>|]+)(?:$|(?:,\W?(?:(?<Version>Version=(?<VersionValue>(?:\d{1,2}\.?){1,4}))|(?<Culture>Culture=(?<CultureValue>neutral|\w{2}-\w{2}))|(?<PublicKeyToken>PublicKeyToken=(?<PublicKeyTokenValue>[A-Fa-f0-9]{16})))(?:,\W?)?){3})))$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"0"*32+"!1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^(?<Namespace>(?:[\w][\w\d]*\.?)*)\.(?<Class>[\w][\w\d<>]*(?:(?:\+[\w][\w\d<>]*)+|))(?:|,\W?(?<Assembly>(?<AssemblyName>[^\W/\\:*?"<>|]+)(?:$|(?:,\W?(?:(?<Version>Version=(?<VersionValue>(?:\d{1,2}\.?){1,4}))|(?<Culture>Culture=(?<CultureValue>neutral|\w{2}-\w{2}))|(?<PublicKeyToken>PublicKeyToken=(?<PublicKeyTokenValue>[A-Fa-f0-9]{16})))(?:,\W?)?){3})))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 1 + "!1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")