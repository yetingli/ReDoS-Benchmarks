import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_6179 {
    /* 6179
     * ^(ftp|https?):\/\/([^:]+:[^@]*@)?([a-zA-Z0-9][-_a-zA-Z0-9]*\.)*([a-zA-Z0-9][-_a-zA-Z0-9]*){1}(:[0-9]+)?\/?(((\/|\[|\]|-|~|_|\.|:|[a-zA-Z0-9]|%[0-9a-fA-F]{2})*)\?((\/|\[|\]|-|~|_|\.|,|:|=||\{|\}|[a-zA-Z0-9]|%[0-9a-fA-F]{2})*\&?)*)?(#([-_.a-zA-Z0-9]|%[a-fA-F0-9]{2})*)?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"ftp://a?"+"/"*16+"! _1_NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(ftp|https?):\\/\\/([^:]+:[^@]*@)?([a-zA-Z0-9][-_a-zA-Z0-9]*\\.)*([a-zA-Z0-9][-_a-zA-Z0-9]*){1}(:[0-9]+)?\\/?(((\\/|\\[|\\]|-|~|_|\\.|:|[a-zA-Z0-9]|%[0-9a-fA-F]{2})*)\\?((\\/|\\[|\\]|-|~|_|\\.|,|:|=||\\{|\\}|[a-zA-Z0-9]|%[0-9a-fA-F]{2})*\\&?)*)?(#([-_.a-zA-Z0-9]|%[a-fA-F0-9]{2})*)?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("ftp://a?");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("/");
            }
            // 后缀
            attackString.append("! _1_NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
