import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2750 {
    /* 2750
     * ^(?<From>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9])+)(-|–|:|TO)?(?<To>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9]|PRESENT)+)+(:)*
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"JUNE "*16+"! _1_EOD(i2)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?<From>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9])+)(-|–|:|TO)?(?<To>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9]|PRESENT)+)+(:)*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("JUNE ");
            }
            // 后缀
            attackString.append("! _1_EOD(i2)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
