#vuln pattern: SLQ
#vuln degree: POL
#mul vuln: N
#vuln location: 0-1


import re2 as re
from time import perf_counter

regex = '.*(?=tt\d)'
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i*1000 + "!"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = re.search(regex, ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{LEN}: took {DURATION} seconds!")






#
# if __name__ == '__main__':
#
#     print(re.match('x*a', 'axx').span(0))
#     # file_path = r"E:\result\large\snort.txt"
#     # with open(file_path, encoding='utf-8') as f:
#     #     for line in f.readlines():
    #         line = line.replace("\n", "")
    #         cnt = line.count(r"\b")
    #         if cnt ==1:
    #             if line.startswith(r"\b")!=True and line.endswith(r"\b")!=True:
    #                 print(line)
    #
    # # file_path = r"E:\result\large\snort\tmp6.txt"
    # # with open(file_path, encoding='utf-8') as f:
    # #     for line in f.readlines():
    # #         line = line.replace("\n", "")
    # #         cnt = line.count("+") + line.count("*") + line.count("{") - (line.count("\+") + line.count("\*") + line.count("\{"))
    # #
    # #         if cnt<=4:
    # #         # if line.find(r".*(?P<v>(\w\x00)+")!=-1:
    # #             pass
    # #             print(line)
    # #             print(line[line.rfind(" ")+1:])
    # #         else:
    # #             write_add(r"E:\result\large\snort\tmp7.txt", line+"\n")