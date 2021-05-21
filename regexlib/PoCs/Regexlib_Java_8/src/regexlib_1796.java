import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1796 {
    /* 1796
     * target[ ]*[=]([ ]*)([&quot;]|['])*([_])*([A-Za-z0-9])+([&quot;])*
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"target="+"o"*1024+"!1 _!1 _!1 _! _1!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "target[ ]*[=]([ ]*)([&quot;]|[\'])*([_])*([A-Za-z0-9])+([&quot;])*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("target=");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("o");
            }
            // 后缀
            attackString.append("!1 _!1 _!1 _! _1!\n_SLQ_3");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
