import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3232 {
    /* 3232
     * [a-z0-9][a-z0-9_\.-]{0,}[a-z0-9]\.[a-z0-9][a-z0-9_\.-]{0,}[a-z0-9][\.][cn]{2,4}
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"a"+"0.0"*5000+"!1 __POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "[a-z0-9][a-z0-9_\\.-]{0,}[a-z0-9]\\.[a-z0-9][a-z0-9_\\.-]{0,}[a-z0-9][\\.][cn]{2,4}";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("a");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("0.0");
            }
            // 后缀
            attackString.append("!1 __POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}