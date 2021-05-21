# 3277
# (http):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+(\\.[\\w\\-_]+)(\\/)([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?^=%&amp;/~\\+#]+)(\\/)((\\d{8}-)|(\\d{9}-)|(\\d{10}-)|(\\d{11}-))+([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?+html^])?
# EXPONENT
# nums:4
# EXPONENT AttackString:"http:\\/\\/\\"+"\\\\"*32+"! _1_EOA(iv)"

import re
from time import perf_counter

regex = """(http):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+(\\.[\\w\\-_]+)(\\/)([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?^=%&amp;/~\\+#]+)(\\/)((\\d{8}-)|(\\d{9}-)|(\\d{10}-)|(\\d{11}-))+([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?+html^])?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http:\\/\\/\\" + "\\\\" * i * 1 + "! _1_EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")