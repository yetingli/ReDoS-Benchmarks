import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8244 {
    /* 8244
     * ^.*[_A-Za-z0-9]+[\t ]+[\*&]?[\t ]*[_A-Za-z0-9](::)?[_A-Za-z0-9:]+[\t ]*\(( *[ \[\]\*&A-Za-z0-9_]+ *,? *)*\).*$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"_\t__("+" "*16+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^.*[_A-Za-z0-9]+[\\t ]+[\\*&]?[\\t ]*[_A-Za-z0-9](::)?[_A-Za-z0-9:]+[\\t ]*\\(( *[ \\[\\]\\*&A-Za-z0-9_]+ *,? *)*\\).*$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("_\t__(");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(" ");
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
