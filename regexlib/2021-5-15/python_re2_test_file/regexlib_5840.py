# 5840
# ((http|ftp|https):\/\/w{3}[\d]*.|(http|ftp|https):\/\/|w{3}[\d]*.)([\w\d\._\-#\(\)\[\]\\,;:]+@[\w\d\._\-#\(\)\[\]\\,;:])?([a-z0-9]+.)*[a-z\-0-9]+.([a-z]{2,3})?[a-z]{2,6}(:[0-9]+)?(\/[\/a-z0-9\._\-,]+)*[a-z0-9\-_\.\s\%]+(\?[a-z0-9=%&amp;\.\-,#]+)?
# EXPONENT
# nums:5
# EXPONENT AttackString:"http://www1a1aa"+"/"*32+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """((http|ftp|https):\/\/w{3}[\d]*.|(http|ftp|https):\/\/|w{3}[\d]*.)([\w\d\._\-#\(\)\[\]\\,;:]+@[\w\d\._\-#\(\)\[\]\\,;:])?([a-z0-9]+.)*[a-z\-0-9]+.([a-z]{2,3})?[a-z]{2,6}(:[0-9]+)?(\/[\/a-z0-9\._\-,]+)*[a-z0-9\-_\.\s\%]+(\?[a-z0-9=%&amp;\.\-,#]+)?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "http://www1a1aa" + "/" * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")