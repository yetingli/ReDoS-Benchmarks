import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4135 {
    /* 4135
     * ("(?!")(""|[^"])*("|$)|\S)+/g
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+""!"*32+"! _1_EOD(i4)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(\"(?!\")(\"\"|[^\"])*(\"|$)|\\S)+/g";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\"!");
            }
            // 后缀
            attackString.append("! _1_EOD(i4)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
