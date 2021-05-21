import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7920 {
    /* 7920
     * ^v=spf1[ \t]+[+?~-]?(?:(?:all)|(?:ip4(?:[:][0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})?(?:/[0-9]{1,2})?)|(?:ip6(?:[:]([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})?(?:/[0-9]{1,2})?)|(?:a(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:mx(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:ptr(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exists(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:include(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:redirect(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exp(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|)(?:(?:[ \t]+[+?~-]?(?:(?:all)|(?:ip4(?:[:][0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})?(?:/[0-9]{1,2})?)|(?:ip6(?:[:]([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})?(?:/[0-9]{1,2})?)|(?:a(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:mx(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:ptr(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exists(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:include(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:redirect(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exp(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|))*)?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"v=spf1 "+" "*32+"! _1_NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^v=spf1[ \\t]+[+?~-]?(?:(?:all)|(?:ip4(?:[:][0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})?(?:/[0-9]{1,2})?)|(?:ip6(?:[:]([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})?(?:/[0-9]{1,2})?)|(?:a(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:mx(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:ptr(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exists(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:include(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:redirect(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exp(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|)(?:(?:[ \\t]+[+?~-]?(?:(?:all)|(?:ip4(?:[:][0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})?(?:/[0-9]{1,2})?)|(?:ip6(?:[:]([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})?(?:/[0-9]{1,2})?)|(?:a(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:mx(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+)?(?:/[0-9]{1,2})?)|(?:ptr(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exists(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:include(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:redirect(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|(?:exp(?:[:][A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+))|))*)?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("v=spf1 ");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(" ");
            }
            // 后缀
            attackString.append("! _1_NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
