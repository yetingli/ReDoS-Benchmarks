import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2073 {
    /* 2073
     * (?<FirstName>[A-Z]\.?\w*\-?[A-Z]?\w*)\s?(?<MiddleName>[A-Z]\w+|[A-Z]?\.?)\s(?<LastName>[A-Z]?\w{0,3}[A-Z]\w+\-?[A-Z]?\w*)(?:,\s|)(?<Suffix>Jr\.|Sr\.|IV|III|II|)
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"AA1 "+"A1"*512+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?<FirstName>[A-Z]\\.?\\w*\\-?[A-Z]?\\w*)\\s?(?<MiddleName>[A-Z]\\w+|[A-Z]?\\.?)\\s(?<LastName>[A-Z]?\\w{0,3}[A-Z]\\w+\\-?[A-Z]?\\w*)(?:,\\s|)(?<Suffix>Jr\\.|Sr\\.|IV|III|II|)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("AA1 ");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("A1");
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
