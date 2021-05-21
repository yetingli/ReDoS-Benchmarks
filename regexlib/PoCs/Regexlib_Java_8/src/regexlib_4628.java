import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4628 {
    /* 4628
     * ^\d*[0-9](|.\d*[0-9]|,\d*[0-9])?$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"0"+"1"*10000+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^\\d*[0-9](|.\\d*[0-9]|,\\d*[0-9])?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("0");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("1");
            }
            // 后缀
            attackString.append("! _1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}