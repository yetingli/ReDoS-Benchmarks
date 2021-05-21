import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5839 {
    /* 5839
     * &lt;(?:[^&quot;']+?|.+?(?:&quot;|').*?(?:&quot;|')?.*?)*?&gt;
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"&lt;"+"'"*2+"! _1! _1! _1! _1! _1!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "&lt;(?:[^&quot;\']+?|.+?(?:&quot;|\').*?(?:&quot;|\')?.*?)*?&gt;";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("&lt;");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\'");
            }
            // 后缀
            attackString.append("! _1! _1! _1! _1! _1!\n_SLQ_3");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
