import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8548 {
    /* 8548
     * (?:\b\w*(\w\w?)\1{2,}\w*\b)
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"111"+"00"*512+"! _1_EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:\\b\\w*(\\w\\w?)\\1{2,}\\w*\\b)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("111");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("00");
            }
            // 后缀
            attackString.append("! _1_EOA(iii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
