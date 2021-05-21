import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1672 {
    /* 1672
     * \s*([a-z\. ]+)\s*\n\s*([a-z0-9\. #]+)\s*\n\s*([a-z \.]+)\s*,\s*([a-z \.]+)\s*\n?(?:\s*(\d{1,15}(?:-\d{1,4})?)\s*\n)?(?:\s*(\+?(?:1\s*[-\/\.]?)?(?:\((?:\d{3})\)|(?:\d{3}))\s*[-\/\.]?\s*(?:\d{3})\s*[-\/\.]?\s*(?:\d{4})(?:(?:[ \t]*[xX]|[eE][xX][tT])\.?[ \t]*(?:\d+))*))?
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"a"*10000+"!_1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "\\s*([a-z\\. ]+)\\s*\\n\\s*([a-z0-9\\. #]+)\\s*\\n\\s*([a-z \\.]+)\\s*,\\s*([a-z \\.]+)\\s*\\n?(?:\\s*(\\d{1,15}(?:-\\d{1,4})?)\\s*\\n)?(?:\\s*(\\+?(?:1\\s*[-\\/\\.]?)?(?:\\((?:\\d{3})\\)|(?:\\d{3}))\\s*[-\\/\\.]?\\s*(?:\\d{3})\\s*[-\\/\\.]?\\s*(?:\\d{4})(?:(?:[ \\t]*[xX]|[eE][xX][tT])\\.?[ \\t]*(?:\\d+))*))?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("a");
            }
            // 后缀
            attackString.append("!_1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
