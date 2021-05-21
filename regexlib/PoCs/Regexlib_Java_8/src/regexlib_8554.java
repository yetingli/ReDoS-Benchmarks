import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8554 {
    /* 8554
     * ^((([!#$%&'*+\-/=?^_`{|}~\w])|([!#$%&'*+\-/=?^_`{|}~\w][!#$%&'*+\-/=?^_`{|}~\.\w]{0,}[!#$%&'*+\-/=?^_`{|}~\w]))[@]\w+([-.]\w+)*\.\w+([-.]\w+)*)$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"!@1"+".0"*5000+"@1 __POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((([!#$%&\'*+\\-/=?^_`{|}~\\w])|([!#$%&\'*+\\-/=?^_`{|}~\\w][!#$%&\'*+\\-/=?^_`{|}~\\.\\w]{0,}[!#$%&\'*+\\-/=?^_`{|}~\\w]))[@]\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*)$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("!@1");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append(".0");
            }
            // 后缀
            attackString.append("@1 __POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
