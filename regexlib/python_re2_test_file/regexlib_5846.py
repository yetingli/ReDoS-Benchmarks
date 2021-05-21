# 5846
# ((http|ftp|https|ftps):\/\/)?[\w\-_\.]+\.(([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(:[0-9]+)?\/?(([\w\-\.,@^%:/~\+#]*[\w\-\@^%/~\+#])((\?[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)+(&[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)*)?)?
# EXPONENT
# nums:5
# EXPONENT AttackString:"1.aaa"+"aa"*32+"! _1_NQ"

import re2 as re
from time import perf_counter

regex = """((http|ftp|https|ftps):\/\/)?[\w\-_\.]+\.(([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(:[0-9]+)?\/?(([\w\-\.,@^%:/~\+#]*[\w\-\@^%/~\+#])((\?[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)+(&[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)*)?)?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1.aaa" + "aa" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")