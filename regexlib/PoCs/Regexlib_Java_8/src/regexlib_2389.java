import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2389 {
    /* 2389
     * (\s*\(?0\d{4}\)?(\s*|-)\d{3}(\s*|-)\d{3}\s*)|(\s*\(?0\d{3}\)?(\s*|-)\d{3}(\s*|-)\d{4}\s*)|(\s*(7|8)(\d{7}|\d{3}(\-|\s{1})\d{4})\s*)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+" "*5000+"! _1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(\\s*\\(?0\\d{4}\\)?(\\s*|-)\\d{3}(\\s*|-)\\d{3}\\s*)|(\\s*\\(?0\\d{3}\\)?(\\s*|-)\\d{3}(\\s*|-)\\d{4}\\s*)|(\\s*(7|8)(\\d{7}|\\d{3}(\\-|\\s{1})\\d{4})\\s*)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append(" ");
            }
            // 后缀
            attackString.append("! _1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
