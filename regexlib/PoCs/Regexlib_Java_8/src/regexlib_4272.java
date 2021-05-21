import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4272 {
    /* 4272
     * ^(((\.\.){1}/)*|(/){1})?(([a-zA-Z0-9]*)/)*([a-zA-Z0-9]*)+([.jpg]|[.gif])+$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"f"*32+"!1 _!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(((\\.\\.){1}/)*|(/){1})?(([a-zA-Z0-9]*)/)*([a-zA-Z0-9]*)+([.jpg]|[.gif])+$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("f");
            }
            // 后缀
            attackString.append("!1 _!\n_SLQ_3");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
