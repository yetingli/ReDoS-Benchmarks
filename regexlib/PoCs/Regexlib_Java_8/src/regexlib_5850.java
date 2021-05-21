import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5850 {
    /* 5850
     * (?<username>#?[+_a-zA-Z0-9+-]+(\.[+_a-zA-Z0-9+-]+)*)@(?<domain>[a-zA-Z0-9]+(-(?!-)|[a-zA-Z0-9\.])*?[a-zA-Z0-9]+\.([0-9]{1,3}|[a-zA-Z]{2,3}|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel)))
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"+@a"+"B"*512+"! _1!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?<username>#?[+_a-zA-Z0-9+-]+(\\.[+_a-zA-Z0-9+-]+)*)@(?<domain>[a-zA-Z0-9]+(-(?!-)|[a-zA-Z0-9\\.])*?[a-zA-Z0-9]+\\.([0-9]{1,3}|[a-zA-Z]{2,3}|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel)))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("+@a");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("B");
            }
            // 后缀
            attackString.append("! _1!\n_SLQ_3");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
