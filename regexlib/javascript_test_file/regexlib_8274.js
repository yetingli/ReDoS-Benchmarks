/* 8274
 * ^(((?:C/[-O]?[a-z\ ]*?)?\ *)?(P[\.\ ]?O[\.\ ]?\ ?Box\ *\d+)|(?:((?:C/[-O]?)?[\w\ ,\.']+?),?/?\ *?)?\ *?\b((?:\d+-)?\d+[a-z]?)[\ ](((?:[\w\ '-]|st)+)(?:\b(ALLEY|ALLY|APPROACH|APP|ARCADE|ARC|AVENUE|AVE|BOULEVARD|BLVD|BROW|BYPASS|BYPA|CAUSEWAY|CWAY|CIRCUIT|CCT|CIRCUS|CIRC|CLOSE|CL|COPSE|CPSE|CORNER|CNR|COVE|COURT|CRT|CT|CRESCENT|CRES|DRIVE|DR|END|ESPLANANDE|ESP|FLAT|FREEWAY|FWAY|FRONTAGE|FRNT|GARDENS|GDNS|GLADE|GLD|GLEN|GREEN|GRN|GROVE|GR|HEIGHTS|HTS|HIGHWAY|HWY|LANE|LINK|LOOP|MALL|MEWS|PACKET|PCKT|PARADE|PDE|PARK|PARKWAY|PKWY|PLACE|PL|PROMENADE|PROM|RESERVE|RES|RIDGE|RDGE|RISE|ROAD|RD|ROW|SQUARE|SQ|STREET|ST|STRIP|STRP|TARN|TERRACE|TCE|THOROUGHFARE|TFRE|TRACK|TRAC|TRUNKWAY|TWAY|VIEW|VISTA|VSTA|WALK|WAY|WALKWAY|WWAY|YARD )\b)))(?:,?\ *?([a-z'.]+(?:,?\ +[a-z'.]+)*?))?(?:,?\ *?(Victoria|VIC|New South Wales|NSW|South Australia|SA|Northern Territory|NT|West Australia|WA|Tasmania|TAS|Australian Capital Territory|ACT|Queensland|QLD))?(?:,?\ *?(\d{3,4}))?(?:,?\ *?(Au(?:stralia)?))?(?:(?=[^$])\s)*$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"aPOBox1"+" "*512+"!1 _SLQ_2"
 */
var REGEX = new RegExp("^(((?:C/[-O]?[a-z\ ]*?)?\ *)?(P[\.\ ]?O[\.\ ]?\ ?Box\ *\d+)|(?:((?:C/[-O]?)?[\w\ ,\.']+?),?/?\ *?)?\ *?\b((?:\d+-)?\d+[a-z]?)[\ ](((?:[\w\ '-]|st)+)(?:\b(ALLEY|ALLY|APPROACH|APP|ARCADE|ARC|AVENUE|AVE|BOULEVARD|BLVD|BROW|BYPASS|BYPA|CAUSEWAY|CWAY|CIRCUIT|CCT|CIRCUS|CIRC|CLOSE|CL|COPSE|CPSE|CORNER|CNR|COVE|COURT|CRT|CT|CRESCENT|CRES|DRIVE|DR|END|ESPLANANDE|ESP|FLAT|FREEWAY|FWAY|FRONTAGE|FRNT|GARDENS|GDNS|GLADE|GLD|GLEN|GREEN|GRN|GROVE|GR|HEIGHTS|HTS|HIGHWAY|HWY|LANE|LINK|LOOP|MALL|MEWS|PACKET|PCKT|PARADE|PDE|PARK|PARKWAY|PKWY|PLACE|PL|PROMENADE|PROM|RESERVE|RES|RIDGE|RDGE|RISE|ROAD|RD|ROW|SQUARE|SQ|STREET|ST|STRIP|STRP|TARN|TERRACE|TCE|THOROUGHFARE|TFRE|TRACK|TRAC|TRUNKWAY|TWAY|VIEW|VISTA|VSTA|WALK|WAY|WALKWAY|WWAY|YARD )\b)))(?:,?\ *?([a-z'.]+(?:,?\ +[a-z'.]+)*?))?(?:,?\ *?(Victoria|VIC|New South Wales|NSW|South Australia|SA|Northern Territory|NT|West Australia|WA|Tasmania|TAS|Australian Capital Territory|ACT|Queensland|QLD))?(?:,?\ *?(\d{3,4}))?(?:,?\ *?(Au(?:stralia)?))?(?:(?=[^$])\s)*$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'aPOBox1' + ' '.repeat(i*1) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}