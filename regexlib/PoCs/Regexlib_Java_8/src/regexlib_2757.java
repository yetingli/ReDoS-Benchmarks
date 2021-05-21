import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2757 {
    /* 2757
     * ^\s*-?(\d{0,7}|10[0-5]\d{0,5}|106[0-6]\d{0,4}|1067[0-4]\d{0,3}|10675[0-1]\d{0,2}|((\d{0,7}|10[0-5]\d{0,5}|106[0-6]\d{0,4}|1067[0-4]\d{0,3}|10675[0-1]\d{0,2})\.)?([0-1]?[0-9]|2[0-3]):[0-5]?[0-9](:[0-5]?[0-9](\.\d{1,7})?)?)\s*$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"\t"*10000+"!_1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^\\s*-?(\\d{0,7}|10[0-5]\\d{0,5}|106[0-6]\\d{0,4}|1067[0-4]\\d{0,3}|10675[0-1]\\d{0,2}|((\\d{0,7}|10[0-5]\\d{0,5}|106[0-6]\\d{0,4}|1067[0-4]\\d{0,3}|10675[0-1]\\d{0,2})\\.)?([0-1]?[0-9]|2[0-3]):[0-5]?[0-9](:[0-5]?[0-9](\\.\\d{1,7})?)?)\\s*$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("\t");
            }
            // 后缀
            attackString.append("!_1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
