import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4820 {
    /* 4820
     * ([0-9a-zA-Z]+)|([0-9a-zA-Z][0-9a-zA-Z\\s]+[0-9a-zA-Z]+)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"0"*10000+"SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "([0-9a-zA-Z]+)|([0-9a-zA-Z][0-9a-zA-Z\\\\s]+[0-9a-zA-Z]+)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("0");
            }
            // 后缀
            attackString.append("SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
