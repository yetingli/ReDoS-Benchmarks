import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8482 {
    /* 8482
     * ((MON|TUE|WED|THU|FRI|SAT|SUN)[A-Z]*)*[\ ,-]*(\d|\d{2})*(st|nd|rd|th)*[\ ,-]*(JAN|FEB|MAR|MAY|APR|JUL|JUN|AUG|OCT|SEP|NOV|DEC)[A-Z]*[\ ,]*(\d|\d{2}|\d{4})*(st|nd|rd|th)*([\ ,])*'*(\d{2}|\d{4})*\b
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"JAN"+"00"*16+"! _1_EOD(i4)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((MON|TUE|WED|THU|FRI|SAT|SUN)[A-Z]*)*[\\ ,-]*(\\d|\\d{2})*(st|nd|rd|th)*[\\ ,-]*(JAN|FEB|MAR|MAY|APR|JUL|JUN|AUG|OCT|SEP|NOV|DEC)[A-Z]*[\\ ,]*(\\d|\\d{2}|\\d{4})*(st|nd|rd|th)*([\\ ,])*\'*(\\d{2}|\\d{4})*\\b";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("JAN");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("00");
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
