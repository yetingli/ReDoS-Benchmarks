import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2337 {
    /* 2337
     * ^<a[^>]*(http://[^"]*)[^>]*>([ 0-9a-zA-Z]+)</a>$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"<a"+"http://"*256+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^<a[^>]*(http://[^\"]*)[^>]*>([ 0-9a-zA-Z]+)</a>$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<a");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("http://");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
