import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1815 {
    /* 1815
     * (((ht|f)tp(s?):\/\/)|(www\.[^ \[\]\(\)\n\r\t]+)|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})\/)([^ \[\]\(\),;&quot;'&lt;&gt;\n\r\t]+)([^\. \[\]\(\),;&quot;'&lt;&gt;\n\r\t])|(([012]?[0-9]{1,2}\.){3}[012]?[0-9]{1,2})
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"www.!"*5000+"! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(((ht|f)tp(s?):\\/\\/)|(www\\.[^ \\[\\]\\(\\)\\n\\r\\t]+)|(([012]?[0-9]{1,2}\\.){3}[012]?[0-9]{1,2})\\/)([^ \\[\\]\\(\\),;&quot;\'&lt;&gt;\\n\\r\\t]+)([^\\. \\[\\]\\(\\),;&quot;\'&lt;&gt;\\n\\r\\t])|(([012]?[0-9]{1,2}\\.){3}[012]?[0-9]{1,2})";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("www.!");
            }
            // 后缀
            attackString.append("! _1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
