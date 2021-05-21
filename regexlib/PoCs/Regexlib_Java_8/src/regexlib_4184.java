import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4184 {
//    /* 4184
//     * ((http|https|ftp|telnet|gopher|ms\-help|file|notes)://)?(([a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)(:.*)?@)?(([a-z0-9][\w\-]*[a-z0-9]*\.)*(((([a-z0-9][\w\-]*[a-z0-9]*)(\.[a-z0-9]+)?)|(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))(:[0-9]+)?))?(((/([\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(%\d\d))+)*/([\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(%\d\d))*)(\?[^#]+)?(#[a-z0-9]\w*)?)?
//     * EXPONENT
//     * nums:2
//     * EXPONENT AttackString:""+"00."*32+"! _1_EOA(i or ii)"
//     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((http|https|ftp|telnet|gopher|ms\\-help|file|notes)://)?(([a-z][\\w~%!&amp;\',;=\\-\\.$\\(\\)\\*\\+]*)(:.*)?@)?(([a-z0-9][\\w\\-]*[a-z0-9]*\\.)*(((([a-z0-9][\\w\\-]*[a-z0-9]*)(\\.[a-z0-9]+)?)|(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))(:[0-9]+)?))?(((/([\\w`~!$=;\\-\\+\\.\\^\\(\\)\\|\\{\\}\\[\\]]|(%\\d\\d))+)*/([\\w`~!$=;\\-\\+\\.\\^\\(\\)\\|\\{\\}\\[\\]]|(%\\d\\d))*)(\\?[^#]+)?(#[a-z0-9]\\w*)?)?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("00.");
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
