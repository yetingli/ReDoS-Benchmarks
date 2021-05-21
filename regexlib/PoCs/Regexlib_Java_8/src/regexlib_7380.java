import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7380 {
    /* 7380
     * ((ht|f)tp(s?))(:((\/\/)(?!\/)))(((w){3}\.)?)([a-zA-Z0-9\-_]+(\.(com|edu|gov|int|mil|net|org|biz|info|name|pro|museum|co\.uk)))(\/(?!\/))(([a-zA-Z0-9\-_\/]*)?)([a-zA-Z0-9])+\.((jpg|jpeg|gif|png)(?!(\w|\W)))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"http://a.com/"+"www"*5000+"! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((ht|f)tp(s?))(:((\\/\\/)(?!\\/)))(((w){3}\\.)?)([a-zA-Z0-9\\-_]+(\\.(com|edu|gov|int|mil|net|org|biz|info|name|pro|museum|co\\.uk)))(\\/(?!\\/))(([a-zA-Z0-9\\-_\\/]*)?)([a-zA-Z0-9])+\\.((jpg|jpeg|gif|png)(?!(\\w|\\W)))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http://a.com/");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("www");
            }
            // 后缀
            attackString.append("! _1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
