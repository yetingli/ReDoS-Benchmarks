import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4552 {
    /* 4552
     * (^[A-ZÀ-Ü]{1}[a-zà-ü']+\s[a-zA-Zà-üÀ-Ü]+((([\s\.'])|([a-zà-ü']+))|[a-zà-ü']+[a-zA-Zà-üÀ-Ü']+))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"Aa "+"a"*5000+"!1 __POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(^[A-ZÀ-Ü]{1}[a-zà-ü\']+\\s[a-zA-Zà-üÀ-Ü]+((([\\s\\.\'])|([a-zà-ü\']+))|[a-zà-ü\']+[a-zA-Zà-üÀ-Ü\']+))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("Aa ");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("a");
            }
            // 后缀
            attackString.append("!1 __POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
