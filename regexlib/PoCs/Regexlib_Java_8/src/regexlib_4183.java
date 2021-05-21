import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4183 {
//    /* 4183
//     * ^(?<scheme>(?:http|https|ftp|telnet|gopher|ms\-help|file|notes)://)?(?:(?<user>[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*):(?<password>.*)?@)?(?:(?<domain>(?:[a-z0-9]\w*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9]\w*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))))(?::(?<port>[0-9]+))?)?(?:(?<path>(?:/(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))+)*/(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))*)(?<params>\?[^#]+)?(?<fragment>#[a-z0-9]\w*)?)?$
//     * EXPONENT
//     * nums:2
//     * EXPONENT AttackString:""+"00."*32+"! _1_EOA(i or ii)"
//     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?<scheme>(?:http|https|ftp|telnet|gopher|ms\\-help|file|notes)://)?(?:(?<user>[a-z][\\w~%!&amp;\',;=\\-\\.$\\(\\)\\*\\+]*):(?<password>.*)?@)?(?:(?<domain>(?:[a-z0-9]\\w*[a-z0-9]*\\.)*(?:(?:(?:[a-z0-9]\\w*[a-z0-9]*)(?:\\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))))(?::(?<port>[0-9]+))?)?(?:(?<path>(?:/(?:[\\w`~!$=;\\-\\+\\.\\^\\(\\)\\|\\{\\}\\[\\]]|(?:%\\d\\d))+)*/(?:[\\w`~!$=;\\-\\+\\.\\^\\(\\)\\|\\{\\}\\[\\]]|(?:%\\d\\d))*)(?<params>\\?[^#]+)?(?<fragment>#[a-z0-9]\\w*)?)?$";
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
