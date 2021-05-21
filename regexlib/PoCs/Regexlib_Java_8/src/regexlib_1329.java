import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1329 {
    /* 1329
     * (https?://)?((?:(\w+-)*\w+)\.)+(?:com|org|net|edu|gov|biz|info|name|museum|[a-z]{2})(\/?\w?-?=?_?\??&?)+[\.]?[a-z0-9\?=&_\-%#]*
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"1.com"+"_"*16+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(https?://)?((?:(\\w+-)*\\w+)\\.)+(?:com|org|net|edu|gov|biz|info|name|museum|[a-z]{2})(\\/?\\w?-?=?_?\\??&?)+[\\.]?[a-z0-9\\?=&_\\-%#]*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("1.com");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("_");
            }
            // 后缀
            attackString.append("! _1_EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
