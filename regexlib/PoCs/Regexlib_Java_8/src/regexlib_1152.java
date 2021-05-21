import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1152 {
    /* 1152
     * (<(tag1|tag2)[^>]*\/?>)[\w\S\s]*?(<\/(?:\2)>)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"<tag1>"*5000+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(<(tag1|tag2)[^>]*\\/?>)[\\w\\S\\s]*?(<\\/(?:\\2)>)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("<tag1>");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
