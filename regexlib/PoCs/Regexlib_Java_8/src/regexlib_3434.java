import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3434 {
    /* 3434
     * \d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\s.\s.\s\[\d{2}\/\D{3}\/\d{4}:\d{1,2}:\d{1,2}:\d{1,2}\s.\d{4}\]\s\&quot;\S*\s\S*\s\S*\&quot;\s\d{1,3}\s\S*\s\&quot;.*\&quot;\s\&quot;.*\&quot;
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"1.1.1.1 1 1 [11/:::/1111:1:1:1 11111] &quot;  &quot; 1  &quot;"*5000+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "\\d{1,3}[.]\\d{1,3}[.]\\d{1,3}[.]\\d{1,3}\\s.\\s.\\s\\[\\d{2}\\/\\D{3}\\/\\d{4}:\\d{1,2}:\\d{1,2}:\\d{1,2}\\s.\\d{4}\\]\\s\\&quot;\\S*\\s\\S*\\s\\S*\\&quot;\\s\\d{1,3}\\s\\S*\\s\\&quot;.*\\&quot;\\s\\&quot;.*\\&quot;";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("1.1.1.1 1 1 [11/:::/1111:1:1:1 11111] &quot;  &quot; 1  &quot;");
            }
            // 后缀
            attackString.append("! _1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
