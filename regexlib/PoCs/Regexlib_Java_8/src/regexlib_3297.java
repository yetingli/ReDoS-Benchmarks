import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3297 {
    /* 3297
     * &lt;a[a-zA-Z0-9 =&quot;'.?_/]*(href\s*=\s*){1}[a-zA-Z0-9 =&quot;'.?_/]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.?_/]*&lt;/a&gt;))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"/&gt;&lt;ahref="+"&gt;"*5000+"!1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "&lt;a[a-zA-Z0-9 =&quot;\'.?_/]*(href\\s*=\\s*){1}[a-zA-Z0-9 =&quot;\'.?_/]*\\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;\'&lt;&gt;.?_/]*&lt;/a&gt;))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("/&gt;&lt;ahref=");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("&gt;");
            }
            // 后缀
            attackString.append("!1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
