import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8377 {
    /* 8377
     * ^((\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2)?)|(?:(?:\2)?(?:\,|\.|\!|\?)?))(?: (\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2|\3)?)|(?:(?:\2|\3)?(?:\,|\.|\!|\?)?)))*)$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"a"+" A'A"*32+"◎@! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((\\\'|\\\")?[a-zA-Z]+(?:\\-[a-zA-Z]+)?(?:s\\\'|\\\'[a-zA-Z]{1,2})?(?:(?:(?:\\,|\\.|\\!|\\?)?(?:\\2)?)|(?:(?:\\2)?(?:\\,|\\.|\\!|\\?)?))(?: (\\\'|\\\")?[a-zA-Z]+(?:\\-[a-zA-Z]+)?(?:s\\\'|\\\'[a-zA-Z]{1,2})?(?:(?:(?:\\,|\\.|\\!|\\?)?(?:\\2|\\3)?)|(?:(?:\\2|\\3)?(?:\\,|\\.|\\!|\\?)?)))*)$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(" A\'A");
            }
            // 后缀
            attackString.append("◎@! _1_EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
