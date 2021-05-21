import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1726 {
    /* 1726
     * class\s+([a-z0-9_]+)(?:\s+extends\s+[a-z0-9_]+)?(?:\s+implements\s+(?:[a-z0-9_]+\s*,*\s*)+)?\s*\{
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"class a"+" implements"*4+"!_1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "class\\s+([a-z0-9_]+)(?:\\s+extends\\s+[a-z0-9_]+)?(?:\\s+implements\\s+(?:[a-z0-9_]+\\s*,*\\s*)+)?\\s*\\{";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("class a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(" implements");
            }
            // 后缀
            attackString.append("!_1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
