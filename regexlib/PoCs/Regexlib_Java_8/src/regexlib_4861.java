import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4861 {
    /* 4861
     * ^[0-9]{6}-(?:[0-9]+){1,3}[0-9A-Za-z]$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"000000-0"+"0"*512+"!1 __NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^[0-9]{6}-(?:[0-9]+){1,3}[0-9A-Za-z]$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("000000-");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("0");
            }
            // 后缀
            attackString.append("!1 __NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
