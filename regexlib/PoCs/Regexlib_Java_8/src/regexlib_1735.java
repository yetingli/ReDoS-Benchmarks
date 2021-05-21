import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1735 {
    /* 1735
     * ^(\w+([_.]{1}\w+)*@\w+([_.]{1}\w+)*\.[A-Za-z]{2,3}[;]?)*$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"1@1"+"_"*32+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(\\w+([_.]{1}\\w+)*@\\w+([_.]{1}\\w+)*\\.[A-Za-z]{2,3}[;]?)*$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("1@1");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("_");
            }
            // 后缀
            attackString.append("! _1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
