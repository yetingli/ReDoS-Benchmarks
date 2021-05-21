import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3374 {
    /* 3374
     * ^([A-Z]{3,20}\s?[A-Z]{2}[0-9]{1,3}-([A-Z]{3}|[A-Z]{1}[0-9]{2}))|([A-Z]{1,20}\s[A-Z]{1,2}[0-9]{1,4}-[A-Z]{1,3})|([\d,\w,\s]{1,20}\s[A-Z]{3}-[0-9]{1,3})|([A-Z]{1,20}\s?[\d,\w,\s]{1,20})$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"A"*80000+"!_1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^([A-Z]{3,20}\\s?[A-Z]{2}[0-9]{1,3}-([A-Z]{3}|[A-Z]{1}[0-9]{2}))|([A-Z]{1,20}\\s[A-Z]{1,2}[0-9]{1,4}-[A-Z]{1,3})|([\\d,\\w,\\s]{1,20}\\s[A-Z]{3}-[0-9]{1,3})|([A-Z]{1,20}\\s?[\\d,\\w,\\s]{1,20})$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("A");
            }
            // 后缀
            attackString.append("!_1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
