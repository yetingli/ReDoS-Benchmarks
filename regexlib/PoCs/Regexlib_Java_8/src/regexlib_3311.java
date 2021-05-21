import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3311 {
    /* 3311
     * \d+\s*[.'-]\s*\d+\s*[\d+.m\"]*
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"1"*10000+"!_1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "\\d+\\s*[.\'-]\\s*\\d+\\s*[\\d+.m\\\"]*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("1");
            }
            // 后缀
            attackString.append("!_1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
