import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7018 {
    /* 7018
     * ^([a-zA-Z](?:(?:(?:\w[\.\_]?)*)\w)+)([a-zA-Z0-9])$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"a"+"_"*32+"!1 __EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^([a-zA-Z](?:(?:(?:\\w[\\.\\_]?)*)\\w)+)([a-zA-Z0-9])$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("_");
            }
            // 后缀
            attackString.append("!1 __EOA(iii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
