import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1516 {
    /* 1516
     * ^(([A-Za-z]+[^0-9]*)([0-9]+[^\W]*)([\W]+[\W0-9A-Za-z]*))|(([A-Za-z]+[^\W]*)([\W]+[^0-9]*)([0-9]+[\W0-9A-Za-z]*))|(([\W]+[^A-Za-z]*)([A-Za-z]+[^0-9]*)([0-9]+[\W0-9A-Za-z]*))|(([\W]+[^0-9]*)([0-9]+[^A-Za-z]*)([A-Za-z]+[\W0-9A-Za-z]*))|(([0-9]+[^A-Za-z]*)([A-Za-z]+[^\W]*)([\W]+[\W0-9A-Za-z]*))|(([0-9]+[^\W]*)([\W]+[^A-Za-z]*)([A-Za-z]+[\W0-9A-Za-z]*))$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"AA0!"+"!"*5000+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(([A-Za-z]+[^0-9]*)([0-9]+[^\\W]*)([\\W]+[\\W0-9A-Za-z]*))|(([A-Za-z]+[^\\W]*)([\\W]+[^0-9]*)([0-9]+[\\W0-9A-Za-z]*))|(([\\W]+[^A-Za-z]*)([A-Za-z]+[^0-9]*)([0-9]+[\\W0-9A-Za-z]*))|(([\\W]+[^0-9]*)([0-9]+[^A-Za-z]*)([A-Za-z]+[\\W0-9A-Za-z]*))|(([0-9]+[^A-Za-z]*)([A-Za-z]+[^\\W]*)([\\W]+[\\W0-9A-Za-z]*))|(([0-9]+[^\\W]*)([\\W]+[^A-Za-z]*)([A-Za-z]+[\\W0-9A-Za-z]*))$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("AA0!");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("!");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
