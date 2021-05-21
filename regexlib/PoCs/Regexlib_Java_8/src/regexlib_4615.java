import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4615 {
    /* 4615
     * &amp;lt;/?([a-zA-Z][-A-Za-z\d\.]{0,71})(\s+(\S+)(\s*=\s*([-\w\.]{1,1024}|&amp;quot;[^&amp;quot;]{0,1024}&amp;quot;|'[^']{0,1024}'))?)*\s*&amp;gt;
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"&amp;lt;a &"+"\t=''"*32+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "&amp;lt;/?([a-zA-Z][-A-Za-z\\d\\.]{0,71})(\\s+(\\S+)(\\s*=\\s*([-\\w\\.]{1,1024}|&amp;quot;[^&amp;quot;]{0,1024}&amp;quot;|\'[^\']{0,1024}\'))?)*\\s*&amp;gt;";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("&amp;lt;a &");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\t=\'\'");
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
