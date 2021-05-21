import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8388 {
    /* 8388
     * ^(/(?:(?:(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*)(?:/(?:(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\-_.!~*'():\@&=+\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*))*))$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"/"+"a"*32+"◎@! _1_NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(/(?:(?:(?:(?:[a-zA-Z0-9\\\\-_.!~*\'():\\@&=+\\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\\\-_.!~*\'():\\@&=+\\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*)(?:/(?:(?:(?:[a-zA-Z0-9\\\\-_.!~*\'():\\@&=+\\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*)(?:;(?:(?:[a-zA-Z0-9\\\\-_.!~*\'():\\@&=+\\$,]+|(?:%[a-fA-F0-9][a-fA-F0-9]))*))*))*))$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("/");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("a");
            }
            // 后缀
            attackString.append("◎@! _1_NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
