import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8038 {
    /* 8038
     * ^(http\://){1}(((www\.){1}([a-zA-Z0-9\-]*\.){1,}){1}|([a-zA-Z0-9\-]*\.){1,10}){1}([a-zA-Z]{2,6}\.){1}([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"http://www.."+"www.www.."*1024+"! _1_EOD(i2)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(http\\://){1}(((www\\.){1}([a-zA-Z0-9\\-]*\\.){1,}){1}|([a-zA-Z0-9\\-]*\\.){1,10}){1}([a-zA-Z]{2,6}\\.){1}([a-zA-Z0-9\\-\\._\\?\\,\\\'/\\\\\\+&amp;%\\$#\\=~])*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http://www..");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("www.www..");
            }
            // 后缀
            attackString.append("! _1_EOD(i2)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
