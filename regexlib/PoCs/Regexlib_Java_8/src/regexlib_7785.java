import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7785 {
    /* 7785
     * ^([A-Z]|[a-z]|[0-9])([A-Z]|[a-z]|[0-9]|([A-Z]|[a-z]|[0-9]|(%|&|'|\+|\-|@|_|\.|\ )[^%&'\+\-@_\.\ ]|\.$|([%&'\+\-@_\.]\ [^\ ]|\ [%&'\+\-@_\.][^%&'\+\-@_\.])))+$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"A"+"A0"*16+"!1 __EOD(i1)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^([A-Z]|[a-z]|[0-9])([A-Z]|[a-z]|[0-9]|([A-Z]|[a-z]|[0-9]|(%|&|\'|\\+|\\-|@|_|\\.|\\ )[^%&\'\\+\\-@_\\.\\ ]|\\.$|([%&\'\\+\\-@_\\.]\\ [^\\ ]|\\ [%&\'\\+\\-@_\\.][^%&\'\\+\\-@_\\.])))+$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("A");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("A0");
            }
            // 后缀
            attackString.append("!1 __EOD(i1)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
