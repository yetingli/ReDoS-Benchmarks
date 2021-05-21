import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4826 {
    /* 4826
     * (?=^.{1,254}$)(^(?:[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]\.?)+(?:[a-zA-Z]{2,})$)
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"0"*32+"! _1_EOA(iv)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?=^.{1,254}$)(^(?:[a-zA-Z0-9][a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9]\\.?)+(?:[a-zA-Z]{2,})$)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("0");
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
