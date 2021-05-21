import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4902 {
    /* 4902
     * ^(([a-z])+.)+[A-Z]([a-z])+$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"a"*64+"!1 __EOA(iv)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(([a-z])+.)+[A-Z]([a-z])+$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("a");
            }
            // 后缀
            attackString.append("!1 __EOA(iv)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
