import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1694 {
    /* 1694
     * ((A[FGIKLMNPRSUZ]S?X?|DAL?L?A?E?S?|DE|DE[LNRST]L?A?E?H?I?O?S?|DI[AE]?|DOS?|DU|EIT?N?E?|ELS?|EN|ETT?|HAI?|HE[NT]|HIN?A?I?N?R?|HOI|IL|IM|ISA|KA|KE|LAS|LES?|LH?IS?|LOS?|LO?U|MA?C|N[AIY]|O[IP]|SI|T[AEO]N?R?|U[MN][AEOS]?|VAN|VE[LR]|VO[MN]|Y[ENR]|ZU[MR]?) )?((LAS?|LOS?|DEN?R?|ZU) )?[A-Z0/'\.-]+( |$)(SR|JR|II+V?|VI+|[1-9][STRDH]+)?
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"II"*5000+"! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((A[FGIKLMNPRSUZ]S?X?|DAL?L?A?E?S?|DE|DE[LNRST]L?A?E?H?I?O?S?|DI[AE]?|DOS?|DU|EIT?N?E?|ELS?|EN|ETT?|HAI?|HE[NT]|HIN?A?I?N?R?|HOI|IL|IM|ISA|KA|KE|LAS|LES?|LH?IS?|LOS?|LO?U|MA?C|N[AIY]|O[IP]|SI|T[AEO]N?R?|U[MN][AEOS]?|VAN|VE[LR]|VO[MN]|Y[ENR]|ZU[MR]?) )?((LAS?|LOS?|DEN?R?|ZU) )?[A-Z0/\'\\.-]+( |$)(SR|JR|II+V?|VI+|[1-9][STRDH]+)?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("II");
            }
            // 后缀
            attackString.append("! _1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
