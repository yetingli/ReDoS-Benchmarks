import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3210 {
    /* 3210
     * ^(?:(?:[\+]?(?<CountryCode>[\d]{1,3}(?:[ ]+|[\-.])))?[(]?(?<AreaCode>[\d]{3})[\-/)]?(?:[ ]+)?)?(?<Number>[a-zA-Z2-9][a-zA-Z0-9 \-.]{6,})(?:(?:[ ]+|[xX]|(i:ext[\.]?)){1,2}(?<Ext>[\d]{1,5}))?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"aaaaaaa "+" "*512+"!1 __NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?:(?:[\\+]?(?<CountryCode>[\\d]{1,3}(?:[ ]+|[\\-.])))?[(]?(?<AreaCode>[\\d]{3})[\\-/)]?(?:[ ]+)?)?(?<Number>[a-zA-Z2-9][a-zA-Z0-9 \\-.]{6,})(?:(?:[ ]+|[xX]|(i:ext)){1,2}(?<Ext>[\\d]{1,5}))?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("aaaaaaa ");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(" ");
            }
            // 后缀
            attackString.append("!1 __NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
