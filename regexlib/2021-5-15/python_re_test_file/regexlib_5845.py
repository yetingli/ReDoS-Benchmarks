# 5845
# (?<protocol>(http|ftp|https|ftps):\/\/)?(?<site>[\w\-_\.]+\.(?<tld>([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(?<port>:[0-9]+)?\/?)((?<resource>[\w\-\.,@^%:/~\+#]*[\w\-\@^%/~\+#])(?<queryString>(\?[a-zA-Z0-9\[\]\-\._+%\$#\~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\~',]*)+(&[a-zA-Z0-9\[\]\-\._+%\$#\~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\~',]*)*)?)?
# EXPONENT
# nums:4
# EXPONENT AttackString:"1."+"AA"*32+"! _1_NQ"

import re
from time import perf_counter

regex = """(?<protocol>(http|ftp|https|ftps):\/\/)?(?<site>[\w\-_\.]+\.(?<tld>([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(?<port>:[0-9]+)?\/?)((?<resource>[\w\-\.,@^%:/~\+#]*[\w\-\@^%/~\+#])(?<queryString>(\?[a-zA-Z0-9\[\]\-\._+%\$#\~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\~',]*)+(&[a-zA-Z0-9\[\]\-\._+%\$#\~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\~',]*)*)?)?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1." + "AA" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")