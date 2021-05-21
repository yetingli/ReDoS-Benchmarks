import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_118 {
    /* 118
     *  <\/{0,1}(?!\/|b>|i>|p>|a\s|a>|br|em>|ol|li|strong>)[^>]*>
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+" <!/"*10000+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = " <\\/{0,1}(?!\\/|b>|i>|p>|a\\s|a>|br|em>|ol|li|strong>)[^>]*>";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append(" <!/");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
