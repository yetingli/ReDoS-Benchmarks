import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5492 {
    /* 5492
     * ^((\D*[a-z]\D*[A-Z]\D*)|(\D*[A-Z]\D*[a-z]\D*)|(\D*\W\D*[a-z])|(\D*\W\D*[A-Z])|(\D*[a-z]\D*\W)|(\D*[A-Z]\D*\W))$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"aA"*512+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((\\D*[a-z]\\D*[A-Z]\\D*)|(\\D*[A-Z]\\D*[a-z]\\D*)|(\\D*\\W\\D*[a-z])|(\\D*\\W\\D*[A-Z])|(\\D*[a-z]\\D*\\W)|(\\D*[A-Z]\\D*\\W))$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("aA");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
