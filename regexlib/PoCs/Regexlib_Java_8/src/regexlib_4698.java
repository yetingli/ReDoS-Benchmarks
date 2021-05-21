import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4698 {
    /* 4698
     * ([A-Za-z]{0,}[\.\,\s]{0,}[A-Za-z]{1,}[\.\s]{1,}[0-9]{1,2}[\,\s]{0,}[0-9]{4})| ([0-9]{0,4}[-,\s]{0,}[A-Za-z]{3,9}[-,\s]{0,}[0-9]{1,2}[-,\s]{0,}[A-Za-z]{0,8})| ([0-9]{1,4}[\/\.\-][0-9]{1,4}[\/\.\-][0-9]{1,4})
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"A"*1024+"!1 _SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "([A-Za-z]{0,}[\\.\\,\\s]{0,}[A-Za-z]{1,}[\\.\\s]{1,}[0-9]{1,2}[\\,\\s]{0,}[0-9]{4})| ([0-9]{0,4}[-,\\s]{0,}[A-Za-z]{3,9}[-,\\s]{0,}[0-9]{1,2}[-,\\s]{0,}[A-Za-z]{0,8})| ([0-9]{1,4}[\\/\\.\\-][0-9]{1,4}[\\/\\.\\-][0-9]{1,4})";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("A");
            }
            // 后缀
            attackString.append("!1 _SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
