import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3235 {
    /* 3235
     * <img[^>]*src=\"?([^\"]*)\"?([^>]*alt=\"?([^\"]*)\"?)?[^>]*>
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"<imgsrc="+"alt="*64+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "<img[^>]*src=\\\"?([^\\\"]*)\\\"?([^>]*alt=\\\"?([^\\\"]*)\\\"?)?[^>]*>";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<imgsrc=");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("alt=");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
