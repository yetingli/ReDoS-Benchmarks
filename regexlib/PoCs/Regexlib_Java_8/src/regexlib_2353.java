import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2353 {
    /* 2353
     * (((ht|f)tp(s?):\/\/)|(([\w]{1,})\.[^ \[\]\(\)\n\r\t]+)|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})\/)([^ \[\]\(\),;"'<>\n\r\t]+)([^\. \[\]\(\),;"'<>\n\r\t])|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"00.00.00."*512+"!1 _◎@! _1@1 _SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(((ht|f)tp(s?):\\/\\/)|(([\\w]{1,})\\.[^ \\[\\]\\(\\)\\n\\r\\t]+)|(([012]?[0-9]{1,2}\\.){3}[012]?[0-9]{1,2})\\/)([^ \\[\\]\\(\\),;\"\'<>\\n\\r\\t]+)([^\\. \\[\\]\\(\\),;\"\'<>\\n\\r\\t])|(([012]?[0-9]{1,2}\\.){3}[012]?[0-9]{1,2})";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("00.00.00.");
            }
            // 后缀
            attackString.append("!1 _◎@! _1@1 _SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
