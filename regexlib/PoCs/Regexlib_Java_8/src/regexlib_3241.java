import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3241 {
//    /* 3241
//     * <[iI][mM][gG][a-zA-Z0-9\s=".]*((src)=\s*(?:"([^"]*)"|'[^']*'))[a-zA-Z0-9\s=".]*/*>(?:</[iI][mM][gG]>)*
//     * POLYNOMIAL
//     * nums:2
//     * POLYNOMIAL AttackString:"<img"+"src="""*5000+"! _1_POA(i)"
//     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "<[iI][mM][gG][a-zA-Z0-9\\s=\".]*((src)=\\s*(?:\"([^\"]*)\"|\'[^\']*\'))[a-zA-Z0-9\\s=\".]*/*>(?:</[iI][mM][gG]>)*";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<img");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("src=\"\"");
            }
            // 后缀
            attackString.append("! _1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
