import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7923 {
    /* 7923
     * &lt;asp:requiredfieldvalidator(\s*\w+\s*=\s*\&quot;?\s*\w+\s*\&quot;?\s*)+\s*&gt;\s*&lt;\/asp:requiredfieldvalidator&gt;
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"&lt;asp:requiredfieldvalidator"+"\t0=&quot0&quot"*32+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "&lt;asp:requiredfieldvalidator(\\s*\\w+\\s*=\\s*\\&quot;?\\s*\\w+\\s*\\&quot;?\\s*)+\\s*&gt;\\s*&lt;\\/asp:requiredfieldvalidator&gt;";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("&lt;asp:requiredfieldvalidator");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\t0=&quot0&quot");
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
