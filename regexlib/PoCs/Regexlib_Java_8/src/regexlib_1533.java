import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1533 {
    /* 1533
     * ^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9]+(-?[a-z0-9]+)?(\.[a-z0-9]+(-?[a-z0-9]+)?)*\.([a-z]{2}|xn\-{2}[a-z0-9]{4,18}|arpa|aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|xxx)$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"_@a"+".000"*16+"!1 __EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^[_a-z0-9-]+(\\.[_a-z0-9-]+)*@[a-z0-9]+(-?[a-z0-9]+)?(\\.[a-z0-9]+(-?[a-z0-9]+)?)*\\.([a-z]{2}|xn\\-{2}[a-z0-9]{4,18}|arpa|aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|xxx)$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("_@a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(".000");
            }
            // 后缀
            attackString.append("!1 __EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
