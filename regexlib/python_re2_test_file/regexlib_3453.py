# 3453
# (?:(?<protocol>http(?:s?)|ftp)(?:\:\/\/))(?:(?<usrpwd>\w+\:\w+)(?:\@))?(?<domain>[^/\r\n\:]+)?(?<port>\:\d+)?(?<path>(?:\/.*)*\/)?(?<filename>.*?\.(?<ext>\w{2,4}))?(?<qrystr>\??(?:\w+\=[^\#]+)(?:\&?\w+\=\w+)*)*(?<bkmrk>\#.*)?
# EXPONENT
# nums:5
# EXPONENT AttackString:"http://"+"/"*32+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(?:(?<protocol>http(?:s?)|ftp)(?:\:\/\/))(?:(?<usrpwd>\w+\:\w+)(?:\@))?(?<domain>[^/\r\n\:]+)?(?<port>\:\d+)?(?<path>(?:\/.*)*\/)?(?<filename>.*?\.(?<ext>\w{2,4}))?(?<qrystr>\??(?:\w+\=[^\#]+)(?:\&?\w+\=\w+)*)*(?<bkmrk>\#.*)?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://" + "/" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")