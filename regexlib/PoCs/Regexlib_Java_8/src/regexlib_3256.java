import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3256 {
    /* 3256
     * ^jdbc:db2://((?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?[.]))*)(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?)))):([0-9]{1,5})/([0-9|A-Z|a-z|_|#|$]{1,16})$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"jdbc:db2://"+"A0."*32+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^jdbc:db2://((?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:(?:(?:[A-Z|a-z])(?:[\\w|-]){0,61}(?:[\\w]?[.]))*)(?:(?:[A-Z|a-z])(?:[\\w|-]){0,61}(?:[\\w]?)))):([0-9]{1,5})/([0-9|A-Z|a-z|_|#|$]{1,16})$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("jdbc:db2://");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("A0.");
            }
            // 后缀
            attackString.append("! _1_EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
