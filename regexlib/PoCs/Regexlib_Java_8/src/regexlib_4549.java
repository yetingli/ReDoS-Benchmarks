import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4549 {
    /* 4549
     * <font[a-zA-Z0-9_\^\$\.\|\{\[\}\]\(\)\*\+\?\\~`!@#%&-=;:'",/\n\s]*>
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"<font"*5000+"◎1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "<font[a-zA-Z0-9_\\^\\$\\.\\|\\{\\[\\}\\]\\(\\)\\*\\+\\?\\\\~`!@#%&-=;:\'\",/\\n\\s]*>";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("<font");
            }
            // 后缀
            attackString.append("◎1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
