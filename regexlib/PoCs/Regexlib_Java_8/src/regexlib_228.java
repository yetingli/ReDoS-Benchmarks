import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_228 {
    /* 228
     * ^([A-Za-z]|[A-Za-z][0-9]*|[0-9]*[A-Za-z])+$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"AA"*8+"!1 __EOD(ii2)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^([A-Za-z]|[A-Za-z][0-9]*|[0-9]*[A-Za-z])+$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("AA");
            }
            // 后缀
            attackString.append("!1 __EOD(ii2)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
