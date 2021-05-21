import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1251 {
    /* 1251
     * ^([a-z0-9]+([\-a-z0-9]*[a-z0-9]+)?\.){0,}([a-z0-9]+([\-a-z0-9]*[a-z0-9]+)?){1,63}(\.[a-z0-9]{2,7})+$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"a"+"00"*8+"!1 __EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^([a-z0-9]+([\\-a-z0-9]*[a-z0-9]+)?\\.){0,}([a-z0-9]+([\\-a-z0-9]*[a-z0-9]+)?){1,63}(\\.[a-z0-9]{2,7})+$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("00");
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
