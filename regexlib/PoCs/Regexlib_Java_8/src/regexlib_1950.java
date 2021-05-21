import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1950 {
    /* 1950
     * ^(?:[^@<>;:,.()\s\[\]\\]+(?:\.(?!@))?)+@(?:[\w\-]+(?:\.(?!\.))?)+\.[A-Za-z]{2,6}$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"-"*32+"@1 __NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?:[^@<>;:,.()\\s\\[\\]\\\\]+(?:\\.(?!@))?)+@(?:[\\w\\-]+(?:\\.(?!\\.))?)+\\.[A-Za-z]{2,6}$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("-");
            }
            // 后缀
            attackString.append("@1 __NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}