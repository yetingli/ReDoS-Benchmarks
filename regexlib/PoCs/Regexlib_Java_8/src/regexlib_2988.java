import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2988 {
    /* 2988
     * ^\s*((?:(?:\d+(?:\x20+\w+\.?)+(?:(?:\x20+STREET|ST|DRIVE|DR|AVENUE|AVE|ROAD|RD|LOOP|COURT|CT|CIRCLE|LANE|LN|BOULEVARD|BLVD)\.?)?)|(?:(?:P\.\x20?O\.|P\x20?O)\x20*Box\x20+\d+)|(?:General\x20+Delivery)|(?:C[\\\/]O\x20+(?:\w+\x20*)+))\,?\x20*(?:(?:(?:APT|BLDG|DEPT|FL|HNGR|LOT|PIER|RM|S(?:LIP|PC|T(?:E|OP))|TRLR|UNIT|\x23)\.?\x20*(?:[a-zA-Z0-9\-]+))|(?:BSMT|FRNT|LBBY|LOWR|OFC|PH|REAR|SIDE|UPPR))?)\,?\s+((?:(?:\d+(?:\x20+\w+\.?)+(?:(?:\x20+STREET|ST|DRIVE|DR|AVENUE|AVE|ROAD|RD|LOOP|COURT|CT|CIRCLE|LANE|LN|BOULEVARD|BLVD)\.?)?)|(?:(?:P\.\x20?O\.|P\x20?O)\x20*Box\x20+\d+)|(?:General\x20+Delivery)|(?:C[\\\/]O\x20+(?:\w+\x20*)+))\,?\x20*(?:(?:(?:APT|BLDG|DEPT|FL|HNGR|LOT|PIER|RM|S(?:LIP|PC|T(?:E|OP))|TRLR|UNIT|\x23)\.?\x20*(?:[a-zA-Z0-9\-]+))|(?:BSMT|FRNT|LBBY|LOWR|OFC|PH|REAR|SIDE|UPPR))?)?\,?\s+((?:[A-Za-z]+\x20*)+)\,\s+(A[BLKSZRAP]|BC|C[AOT]|D[EC]|F[LM]|G[AU]|HI|I[ADLN]|K[SY]|LA|M[ABDEHINOPST]|N[BCDEHJLMSTUVY]|O[HKRN]|P[AERW]|QC|RI|S[CDK]|T[NX]|UT|V[AIT]|W[AIVY]|YT)\s+((\d{5}-\d{4})|(\d{5})|([AaBbCcEeGgHhJjKkLlMmNnPpRrSsTtVvXxYy]\d[A-Za-z]\s?\d[A-Za-z]\d))\s*$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"1 1 C\\O "+"1"*32+"!_1_NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^\\s*((?:(?:\\d+(?:\\x20+\\w+\\.?)+(?:(?:\\x20+STREET|ST|DRIVE|DR|AVENUE|AVE|ROAD|RD|LOOP|COURT|CT|CIRCLE|LANE|LN|BOULEVARD|BLVD)\\.?)?)|(?:(?:P\\.\\x20?O\\.|P\\x20?O)\\x20*Box\\x20+\\d+)|(?:General\\x20+Delivery)|(?:C[\\\\\\/]O\\x20+(?:\\w+\\x20*)+))\\,?\\x20*(?:(?:(?:APT|BLDG|DEPT|FL|HNGR|LOT|PIER|RM|S(?:LIP|PC|T(?:E|OP))|TRLR|UNIT|\\x23)\\.?\\x20*(?:[a-zA-Z0-9\\-]+))|(?:BSMT|FRNT|LBBY|LOWR|OFC|PH|REAR|SIDE|UPPR))?)\\,?\\s+((?:(?:\\d+(?:\\x20+\\w+\\.?)+(?:(?:\\x20+STREET|ST|DRIVE|DR|AVENUE|AVE|ROAD|RD|LOOP|COURT|CT|CIRCLE|LANE|LN|BOULEVARD|BLVD)\\.?)?)|(?:(?:P\\.\\x20?O\\.|P\\x20?O)\\x20*Box\\x20+\\d+)|(?:General\\x20+Delivery)|(?:C[\\\\\\/]O\\x20+(?:\\w+\\x20*)+))\\,?\\x20*(?:(?:(?:APT|BLDG|DEPT|FL|HNGR|LOT|PIER|RM|S(?:LIP|PC|T(?:E|OP))|TRLR|UNIT|\\x23)\\.?\\x20*(?:[a-zA-Z0-9\\-]+))|(?:BSMT|FRNT|LBBY|LOWR|OFC|PH|REAR|SIDE|UPPR))?)?\\,?\\s+((?:[A-Za-z]+\\x20*)+)\\,\\s+(A[BLKSZRAP]|BC|C[AOT]|D[EC]|F[LM]|G[AU]|HI|I[ADLN]|K[SY]|LA|M[ABDEHINOPST]|N[BCDEHJLMSTUVY]|O[HKRN]|P[AERW]|QC|RI|S[CDK]|T[NX]|UT|V[AIT]|W[AIVY]|YT)\\s+((\\d{5}-\\d{4})|(\\d{5})|([AaBbCcEeGgHhJjKkLlMmNnPpRrSsTtVvXxYy]\\d[A-Za-z]\\s?\\d[A-Za-z]\\d))\\s*$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("1 1 C\\O ");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("1");
            }
            // 后缀
            attackString.append("!_1_NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
