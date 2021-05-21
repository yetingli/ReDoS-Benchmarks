import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3031 {
    /* 3031
     * ([0-9]* {0,2}[A-Z]{1}\w+[,.;:]? {0,4}[xvilcXVILC\d]+[.,;:]( {0,2}[\d-,]{1,7})+)([,.;:] {0,4}[xvilcXVILC]*[.,;:]( {0,2}[\d-,]{1,7})+)*
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"A1x.1"+",,"*16+"!1 __EOA(iv)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "([0-9]* {0,2}[A-Z]{1}\\w+[,.;:]? {0,4}[xvilcXVILC\\d]+[.,;:]( {0,2}[\\d-,]{1,7})+)([,.;:] {0,4}[xvilcXVILC]*[.,;:]( {0,2}[\\d-,]{1,7})+)*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("A1x.1");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(",,");
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
