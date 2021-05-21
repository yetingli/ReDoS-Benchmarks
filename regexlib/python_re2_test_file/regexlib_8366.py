# 8366
# (?<STag><)[/\?\s]*(?<Prefix>\w*:)*(?<TagName>\w*)\s*(?<Attributes>(?<Attribute>((?<AttributePrefix>\w*)\s*:\s*)*(?<AttributeName>\w*)\s*=\s*(?<AttributeValue>"[^"]*"|'[^']*'|[^>\s]*)\s*)*)\s*/?(?<ETag>>)
# EXPONENT
# nums:5
# EXPONENT AttackString:"<"+"\t=:''"*32+"! _1_EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """(?<STag><)[/\?\s]*(?<Prefix>\w*:)*(?<TagName>\w*)\s*(?<Attributes>(?<Attribute>((?<AttributePrefix>\w*)\s*:\s*)*(?<AttributeName>\w*)\s*=\s*(?<AttributeValue>"[^"]*"|'[^']*'|[^>\s]*)\s*)*)\s*/?(?<ETag>>)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<" + "\t=:\'\'" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")