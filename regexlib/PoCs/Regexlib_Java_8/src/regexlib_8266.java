import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8266 {
    /* 8266
     * ^(?i:([a-z0-9!#$%^&*{}'`+=-_|/?]+(?:\.[a-z0-9!#$%^&*{}'`+=-_|/?]+)*)@([a-z0-9]+\z?.*[a-z0-9-_]+)*(\.[a-z0-9]{2,}))$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"ia@"+"a"*16+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?i:([a-z0-9!#$%^&*{}\'`+=-_|/?]+(?:\\.[a-z0-9!#$%^&*{}\'`+=-_|/?]+)*)@([a-z0-9]+\\z?.*[a-z0-9-_]+)*(\\.[a-z0-9]{2,}))$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("ia@");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("a");
            }
            // 后缀
            attackString.append("! _1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
