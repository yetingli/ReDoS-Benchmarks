import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2075 {
    /* 2075
     * (?<LastName>[A-Z]\w+\-?[A-Z]?\w*),\s(?<Suffix>Jr\.|Sr\.|IV|III|II)?,?\s?(?<FirstName>[A-Z]\w*\-?[A-Z]?\w*\.?)\s?(?<MiddleName>[A-Z]?\w*\.?)
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"A1, "+"A"*512+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?<LastName>[A-Z]\\w+\\-?[A-Z]?\\w*),\\s(?<Suffix>Jr\\.|Sr\\.|IV|III|II)?,?\\s?(?<FirstName>[A-Z]\\w*\\-?[A-Z]?\\w*\\.?)\\s?(?<MiddleName>[A-Z]?\\w*\\.?)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("A1, ");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("A");
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
