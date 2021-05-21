import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1711 {
    /* 1711
     * ^(958([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+)|(958-([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+)$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"9580000"*16+"!1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(958([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+)|(958-([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+([0-9])+)$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("9580000");
            }
            // 后缀
            attackString.append("!1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
