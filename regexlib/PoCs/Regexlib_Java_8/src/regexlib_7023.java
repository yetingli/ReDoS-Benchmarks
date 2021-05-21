import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7023 {
    /* 7023
     * ^(ht|f)tp(s?)\:\/\/[a-zA-Z0-9\-\._]+(\.[a-zA-Z0-9\-\._]+){2,}(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"http://a.a.a"+"."*32+"! _1_EOA(iv)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(ht|f)tp(s?)\\:\\/\\/[a-zA-Z0-9\\-\\._]+(\\.[a-zA-Z0-9\\-\\._]+){2,}(\\/?)([a-zA-Z0-9\\-\\.\\?\\,\\\'\\/\\\\\\+&amp;%\\$#_]*)?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http://a.a.a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(".");
            }
            // 后缀
            attackString.append("! _1_EOA(iv)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
