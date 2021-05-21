import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8408 {
    /* 8408
     * ^[A-Za-z0-9](\.[\w\-]|[\w\-][\w\-])(\.[\w\-]|[\w\-]?[\w\-]){0,30}[\w\-]?@[A-Za-z0-9\-]{3,63}\.[a-zA-Z]{2,6}$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"A.1"+"-"*32+"!1 __EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^[A-Za-z0-9](\\.[\\w\\-]|[\\w\\-][\\w\\-])(\\.[\\w\\-]|[\\w\\-]?[\\w\\-]){0,30}[\\w\\-]?@[A-Za-z0-9\\-]{3,63}\\.[a-zA-Z]{2,6}$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("A.1");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("-");
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
