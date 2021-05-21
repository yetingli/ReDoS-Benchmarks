import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8274 {
    /* 8274
     * ^(((?:C/[-O]?[a-z\ ]*?)?\ *)?(P[\.\ ]?O[\.\ ]?\ ?Box\ *\d+)|(?:((?:C/[-O]?)?[\w\ ,\.']+?),?/?\ *?)?\ *?\b((?:\d+-)?\d+[a-z]?)[\ ](((?:[\w\ '-]|st)+)(?:\b(ALLEY|ALLY|APPROACH|APP|ARCADE|ARC|AVENUE|AVE|BOULEVARD|BLVD|BROW|BYPASS|BYPA|CAUSEWAY|CWAY|CIRCUIT|CCT|CIRCUS|CIRC|CLOSE|CL|COPSE|CPSE|CORNER|CNR|COVE|COURT|CRT|CT|CRESCENT|CRES|DRIVE|DR|END|ESPLANANDE|ESP|FLAT|FREEWAY|FWAY|FRONTAGE|FRNT|GARDENS|GDNS|GLADE|GLD|GLEN|GREEN|GRN|GROVE|GR|HEIGHTS|HTS|HIGHWAY|HWY|LANE|LINK|LOOP|MALL|MEWS|PACKET|PCKT|PARADE|PDE|PARK|PARKWAY|PKWY|PLACE|PL|PROMENADE|PROM|RESERVE|RES|RIDGE|RDGE|RISE|ROAD|RD|ROW|SQUARE|SQ|STREET|ST|STRIP|STRP|TARN|TERRACE|TCE|THOROUGHFARE|TFRE|TRACK|TRAC|TRUNKWAY|TWAY|VIEW|VISTA|VSTA|WALK|WAY|WALKWAY|WWAY|YARD )\b)))(?:,?\ *?([a-z'.]+(?:,?\ +[a-z'.]+)*?))?(?:,?\ *?(Victoria|VIC|New South Wales|NSW|South Australia|SA|Northern Territory|NT|West Australia|WA|Tasmania|TAS|Australian Capital Territory|ACT|Queensland|QLD))?(?:,?\ *?(\d{3,4}))?(?:,?\ *?(Au(?:stralia)?))?(?:(?=[^$])\s)*$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"aPOBox1"+" "*512+"!1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(((?:C/[-O]?[a-z\\ ]*?)?\\ *)?(P[\\.\\ ]?O[\\.\\ ]?\\ ?Box\\ *\\d+)|(?:((?:C/[-O]?)?[\\w\\ ,\\.\']+?),?/?\\ *?)?\\ *?\\b((?:\\d+-)?\\d+[a-z]?)[\\ ](((?:[\\w\\ \'-]|st)+)(?:\\b(ALLEY|ALLY|APPROACH|APP|ARCADE|ARC|AVENUE|AVE|BOULEVARD|BLVD|BROW|BYPASS|BYPA|CAUSEWAY|CWAY|CIRCUIT|CCT|CIRCUS|CIRC|CLOSE|CL|COPSE|CPSE|CORNER|CNR|COVE|COURT|CRT|CT|CRESCENT|CRES|DRIVE|DR|END|ESPLANANDE|ESP|FLAT|FREEWAY|FWAY|FRONTAGE|FRNT|GARDENS|GDNS|GLADE|GLD|GLEN|GREEN|GRN|GROVE|GR|HEIGHTS|HTS|HIGHWAY|HWY|LANE|LINK|LOOP|MALL|MEWS|PACKET|PCKT|PARADE|PDE|PARK|PARKWAY|PKWY|PLACE|PL|PROMENADE|PROM|RESERVE|RES|RIDGE|RDGE|RISE|ROAD|RD|ROW|SQUARE|SQ|STREET|ST|STRIP|STRP|TARN|TERRACE|TCE|THOROUGHFARE|TFRE|TRACK|TRAC|TRUNKWAY|TWAY|VIEW|VISTA|VSTA|WALK|WAY|WALKWAY|WWAY|YARD )\\b)))(?:,?\\ *?([a-z\'.]+(?:,?\\ +[a-z\'.]+)*?))?(?:,?\\ *?(Victoria|VIC|New South Wales|NSW|South Australia|SA|Northern Territory|NT|West Australia|WA|Tasmania|TAS|Australian Capital Territory|ACT|Queensland|QLD))?(?:,?\\ *?(\\d{3,4}))?(?:,?\\ *?(Au(?:stralia)?))?(?:(?=[^$])\\s)*$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("aPOBox1");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append(" ");
            }
            // 后缀
            attackString.append("!1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
