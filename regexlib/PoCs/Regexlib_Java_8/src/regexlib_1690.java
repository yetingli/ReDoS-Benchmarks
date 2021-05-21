import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1690 {
    /* 1690
     * ^((([a-z0-9])+([\w.-]{1})?)+([^\W_]{1}))+@((([a-z0-9])+([\w-]{1})?)+([^\W_]{1}))+\.[a-z]{2,3}(\.[a-z]{2,4})?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"0"*16+"!1 __EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((([a-z0-9])+([\\w.-]{1})?)+([^\\W_]{1}))+@((([a-z0-9])+([\\w-]{1})?)+([^\\W_]{1}))+\\.[a-z]{2,3}(\\.[a-z]{2,4})?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("0");
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
