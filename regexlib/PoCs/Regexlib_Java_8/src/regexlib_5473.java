import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5473 {
    /* 5473
     * ^\s*([A-Z\s])([a-z\s]){1,30}([A-Z\s])([a-z\s]){1,30}\s*$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"A"+"\t\t"*20000+"!_1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^\\s*([A-Z\\s])([a-z\\s]){1,30}([A-Z\\s])([a-z\\s]){1,30}\\s*$";
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
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
