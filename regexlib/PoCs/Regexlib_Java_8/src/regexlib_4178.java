import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4178 {
    /* 4178
     * ^(?:mailto:)?(?:[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)@(?:[a-z0-9][\w\-]*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9][\w\-]*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"a@250.250.250."+"000"*256+"! _1_EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?:mailto:)?(?:[a-z][\\w~%!&amp;\',;=\\-\\.$\\(\\)\\*\\+]*)@(?:[a-z0-9][\\w\\-]*[a-z0-9]*\\.)*(?:(?:(?:[a-z0-9][\\w\\-]*[a-z0-9]*)(?:\\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("a@250.250.250.");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("000");
            }
            // 后缀
            attackString.append("! _1_EOA(iii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
