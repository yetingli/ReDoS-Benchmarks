import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3471 {
    /* 3471
     * \[bible[=]?([a-zäëïöüæø]*)\]((([0-9][[:space:]]?)?[a-zäëïöüæø]*[[:space:]]{1}([a-zäëïöüæø]*[[:space:]]?[a-zäëïöüæø]*[[:space:]]{1})?)([0-9]{1,3})(:{1}([0-9]{1,3})(-{1}([0-9]{1,3}))?)?)\[\\/bible\]
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"[bible]"+"a"*5000+"◎@! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "\\[bible[=]?([a-zäëïöüæø]*)\\]((([0-9][[:space:]]?)?[a-zäëïöüæø]*[[:space:]]{1}([a-zäëïöüæø]*[[:space:]]?[a-zäëïöüæø]*[[:space:]]{1})?)([0-9]{1,3})(:{1}([0-9]{1,3})(-{1}([0-9]{1,3}))?)?)\\[\\\\/bible\\]";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("[bible]");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("a");
            }
            // 后缀
            attackString.append("◎@! _1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
