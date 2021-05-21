import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4580 {
    /* 4580
     * ((https?|ftp|gopher|telnet|file|notes|ms-help):((//)|(\\\\))+[\w\d:#@%/;$()~_\+-=\\\.&]*)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"http:"+"\\\\\\\\"*5000+"! _1!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((https?|ftp|gopher|telnet|file|notes|ms-help):((//)|(\\\\\\\\))+[\\w\\d:#@%/;$()~_\\+-=\\\\\\.&]*)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http:");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("\\\\\\\\");
            }
            // 后缀
            attackString.append("! _1!\n_SLQ_3");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
