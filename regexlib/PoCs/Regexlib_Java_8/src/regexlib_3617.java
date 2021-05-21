import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3617 {
    /* 3617
     * ^START(?=(?:.(?!END|START))*MIDDLE).*?END[^\n]+
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"START=MIDDLEEND"*5000+"@1 _SLQ_2\n"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^START(?=(?:.(?!END|START))*MIDDLE).*?END[^\\n]+";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("START=MIDDLEEND");
            }
            // 后缀
            attackString.append("@1 _SLQ_2\n");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
