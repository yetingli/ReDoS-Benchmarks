import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8286 {
    /* 8286
     * ^((CN=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(OU=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(DC=['\w\d\s\-\&amp;]+[,]*\s*){1,}(DC=['\w\d\s\-\&amp;]+\s*){1})$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"DC='"+"DC=\t\t"*32+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((CN=([\'\\w\\d\\s\\-\\&amp;\\.]+(\\\\/)*(\\\\,)*)+,\\s*)*(OU=([\'\\w\\d\\s\\-\\&amp;\\.]+(\\\\/)*(\\\\,)*)+,\\s*)*(DC=[\'\\w\\d\\s\\-\\&amp;]+[,]*\\s*){1,}(DC=[\'\\w\\d\\s\\-\\&amp;]+\\s*){1})$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("DC=\'");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("DC=\t\t");
            }
            // 后缀
            attackString.append("! _1_EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
