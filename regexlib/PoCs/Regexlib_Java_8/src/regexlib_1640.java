import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1640 {
    /* 1640
     * <a\s+(?:(?:\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?\s*href\s*=\s*(?<url>\w+|"[^"]*"|'[^']*')(?:(?:\s+\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?>[^<]+</a>
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"<a "+"000="*32+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "<a\\s+(?:(?:\\w+\\s*=\\s*)(?:\\w+|\"[^\"]*\"|\'[^\']*\'))*?\\s*href\\s*=\\s*(?<url>\\w+|\"[^\"]*\"|\'[^\']*\')(?:(?:\\s+\\w+\\s*=\\s*)(?:\\w+|\"[^\"]*\"|\'[^\']*\'))*?>[^<]+</a>";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<a ");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("000=");
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
