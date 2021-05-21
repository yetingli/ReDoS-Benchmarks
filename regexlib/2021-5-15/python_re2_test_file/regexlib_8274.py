# 8274
# ^(((?:C/[-O]?[a-z\ ]*?)?\ *)?(P[\.\ ]?O[\.\ ]?\ ?Box\ *\d+)|(?:((?:C/[-O]?)?[\w\ ,\.']+?),?/?\ *?)?\ *?\b((?:\d+-)?\d+[a-z]?)[\ ](((?:[\w\ '-]|st)+)(?:\b(ALLEY|ALLY|APPROACH|APP|ARCADE|ARC|AVENUE|AVE|BOULEVARD|BLVD|BROW|BYPASS|BYPA|CAUSEWAY|CWAY|CIRCUIT|CCT|CIRCUS|CIRC|CLOSE|CL|COPSE|CPSE|CORNER|CNR|COVE|COURT|CRT|CT|CRESCENT|CRES|DRIVE|DR|END|ESPLANANDE|ESP|FLAT|FREEWAY|FWAY|FRONTAGE|FRNT|GARDENS|GDNS|GLADE|GLD|GLEN|GREEN|GRN|GROVE|GR|HEIGHTS|HTS|HIGHWAY|HWY|LANE|LINK|LOOP|MALL|MEWS|PACKET|PCKT|PARADE|PDE|PARK|PARKWAY|PKWY|PLACE|PL|PROMENADE|PROM|RESERVE|RES|RIDGE|RDGE|RISE|ROAD|RD|ROW|SQUARE|SQ|STREET|ST|STRIP|STRP|TARN|TERRACE|TCE|THOROUGHFARE|TFRE|TRACK|TRAC|TRUNKWAY|TWAY|VIEW|VISTA|VSTA|WALK|WAY|WALKWAY|WWAY|YARD )\b)))(?:,?\ *?([a-z'.]+(?:,?\ +[a-z'.]+)*?))?(?:,?\ *?(Victoria|VIC|New South Wales|NSW|South Australia|SA|Northern Territory|NT|West Australia|WA|Tasmania|TAS|Australian Capital Territory|ACT|Queensland|QLD))?(?:,?\ *?(\d{3,4}))?(?:,?\ *?(Au(?:stralia)?))?(?:(?=[^$])\s)*$
# EXPONENT
# nums:5
# EXPONENT AttackString:"aPOBox1"+" "*512+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(((?:C/[-O]?[a-z\ ]*?)?\ *)?(P[\.\ ]?O[\.\ ]?\ ?Box\ *\d+)|(?:((?:C/[-O]?)?[\w\ ,\.']+?),?/?\ *?)?\ *?\b((?:\d+-)?\d+[a-z]?)[\ ](((?:[\w\ '-]|st)+)(?:\b(ALLEY|ALLY|APPROACH|APP|ARCADE|ARC|AVENUE|AVE|BOULEVARD|BLVD|BROW|BYPASS|BYPA|CAUSEWAY|CWAY|CIRCUIT|CCT|CIRCUS|CIRC|CLOSE|CL|COPSE|CPSE|CORNER|CNR|COVE|COURT|CRT|CT|CRESCENT|CRES|DRIVE|DR|END|ESPLANANDE|ESP|FLAT|FREEWAY|FWAY|FRONTAGE|FRNT|GARDENS|GDNS|GLADE|GLD|GLEN|GREEN|GRN|GROVE|GR|HEIGHTS|HTS|HIGHWAY|HWY|LANE|LINK|LOOP|MALL|MEWS|PACKET|PCKT|PARADE|PDE|PARK|PARKWAY|PKWY|PLACE|PL|PROMENADE|PROM|RESERVE|RES|RIDGE|RDGE|RISE|ROAD|RD|ROW|SQUARE|SQ|STREET|ST|STRIP|STRP|TARN|TERRACE|TCE|THOROUGHFARE|TFRE|TRACK|TRAC|TRUNKWAY|TWAY|VIEW|VISTA|VSTA|WALK|WAY|WALKWAY|WWAY|YARD )\b)))(?:,?\ *?([a-z'.]+(?:,?\ +[a-z'.]+)*?))?(?:,?\ *?(Victoria|VIC|New South Wales|NSW|South Australia|SA|Northern Territory|NT|West Australia|WA|Tasmania|TAS|Australian Capital Territory|ACT|Queensland|QLD))?(?:,?\ *?(\d{3,4}))?(?:,?\ *?(Au(?:stralia)?))?(?:(?=[^$])\s)*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "aPOBox1" + " " * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")