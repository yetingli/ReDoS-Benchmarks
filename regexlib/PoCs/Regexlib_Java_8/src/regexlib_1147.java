import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1147 {
    /* 1147
     * (?<Element>((\*|\w+)?)) (?<Complement>((\.|\#|\-|\w|\:)*)) (?<FamilySeparator>([\s\>\+\~]|[\,\{]))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:" "+"0"*10000+"! _1!1 _◎@! _1!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?<Element>((\\*|\\w+)?)) (?<Complement>((\\.|\\#|\\-|\\w|\\:)*)) (?<FamilySeparator>([\\s\\>\\+\\~]|[\\,\\{]))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("0");
            }
            // 后缀
            attackString.append("");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
