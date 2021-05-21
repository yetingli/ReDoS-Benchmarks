import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3365 {
    /* 3365
     * ([a-zA-Z1-9]*)\.(((a|A)(s|S)(p|P)(x|X))|((h|H)(T|t)(m|M)(l|L))|((h|H)(t|T)(M|m))|((a|A)(s|S)(p|P))|((t|T)(x|X)(T|x))|((m|M)(S|s)(P|p)(x|X))|((g|G)(i|I)(F|f))|((d|D)(o|O)(c|C)))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"a"*10000+"◎@! _1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "([a-zA-Z1-9]*)\\.(((a|A)(s|S)(p|P)(x|X))|((h|H)(T|t)(m|M)(l|L))|((h|H)(t|T)(M|m))|((a|A)(s|S)(p|P))|((t|T)(x|X)(T|x))|((m|M)(S|s)(P|p)(x|X))|((g|G)(i|I)(F|f))|((d|D)(o|O)(c|C)))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("a");
            }
            // 后缀
            attackString.append("◎@! _1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
