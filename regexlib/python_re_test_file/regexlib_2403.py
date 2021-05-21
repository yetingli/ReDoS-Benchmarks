# 2403
# actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=(.*)&pass=(.*)&new_lang=pt_BR&select_view=imp
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=&pass="*256+"! _1SLQ_2"

import re
from time import perf_counter

regex = """actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=(.*)&pass=(.*)&new_lang=pt_BR&select_view=imp"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=&pass=" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")