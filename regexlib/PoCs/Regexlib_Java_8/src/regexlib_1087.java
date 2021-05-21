import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1087 {
    /* 1087
     * ^[^']*?\&lt;\s*Assembly\s*:\s*AssemblyVersion\s*\(\s*&quot;(\*|[0-9]+.\*|[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.[0-9]+)&quot;\s*\)\s*\&gt;.*$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"*01*0101*010101*&lt;Assembly:AssemblyVersion(&quot;"+"0101"*64+"!1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^[^\']*?\\&lt;\\s*Assembly\\s*:\\s*AssemblyVersion\\s*\\(\\s*&quot;(\\*|[0-9]+.\\*|[0-9]+.[0-9]+.\\*|[0-9]+.[0-9]+.[0-9]+.\\*|[0-9]+.[0-9]+.[0-9]+.[0-9]+)&quot;\\s*\\)\\s*\\&gt;.*$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("*01*0101*010101*&lt;Assembly:AssemblyVersion(&quot;");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("0101");
            }
            // 后缀
            attackString.append("!1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
