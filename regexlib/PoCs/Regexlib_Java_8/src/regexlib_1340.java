import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1340 {
    /* 1340
     * ((?<Owner>\[?[\w\d]+\]?)\.{1})?(?<Column>\[?[\w\d]+\]?)(\s*(([><=]{1,2})|(Not|In\(|Between){1,2})\s*)(?<Value>[\w\d\']+)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"1Not"+"Not"*5000+"!1 _◎@! _1!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((?<Owner>\\[?[\\w\\d]+\\]?)\\.{1})?(?<Column>\\[?[\\w\\d]+\\]?)(\\s*(([><=]{1,2})|(Not|In\\(|Between){1,2})\\s*)(?<Value>[\\w\\d\\\']+)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("1Not");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("Not");
            }
            // 后缀
            attackString.append("!1 _◎@! _1!\n_SLQ_3");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
