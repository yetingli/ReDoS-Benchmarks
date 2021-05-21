import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3657 {
    /* 3657
     * &lt;[iI][mM][gG]([^&gt;]*[^/&gt;]*[/&gt;]*[&gt;])
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"&lt;img"+"!"*5000+"! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "&lt;[iI][mM][gG]([^&gt;]*[^/&gt;]*[/&gt;]*[&gt;])";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("&lt;img");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("!");
            }
            // 后缀
            attackString.append("! _1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
