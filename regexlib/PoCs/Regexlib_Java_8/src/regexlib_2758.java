import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2758 {
    /* 2758
     * ^[\s]*(?:(Public|Private)[\s]+(?:[_][\s]*[\n\r]+)?)?(Function|Sub)[\s]+(?:[_][\s]*[\n\r]+)?([a-zA-Z][\w]{0,254})(?:[\s\n\r_]*\((?:[\s\n\r_]*([a-zA-Z][\w]{0,254})[,]?[\s]*)*\))?
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"Function a("+"\tA"*32+"!1 __EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^[\\s]*(?:(Public|Private)[\\s]+(?:[_][\\s]*[\\n\\r]+)?)?(Function|Sub)[\\s]+(?:[_][\\s]*[\\n\\r]+)?([a-zA-Z][\\w]{0,254})(?:[\\s\\n\\r_]*\\((?:[\\s\\n\\r_]*([a-zA-Z][\\w]{0,254})[,]?[\\s]*)*\\))?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("Function a(");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\tA");
            }
            // 后缀
            attackString.append("!1 __EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
