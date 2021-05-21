import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5974 {
    /* 5974
     * ^\s*(\d{0,2})(\.?(\d*))?\s*\%?\s*$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"\t"*5000+"!_1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^\\s*(\\d{0,2})(\\.?(\\d*))?\\s*\\%?\\s*$";
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