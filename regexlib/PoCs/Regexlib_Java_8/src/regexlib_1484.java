import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1484 {
    /* 1484
     * <a[a-zA-Z0-9 ="'.:;?]*(href=[\"\'](http:\/\/|\.\/|\/)?\w+(\.\w+)*(\/\w+(\.\w+)?)*(\/|\?\w*=\w*(&\w*=\w*)*)?[\"\'])*(>[a-zA-Z0-9 ="'<>.:;?]*</a>)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"<a"+"href="0""*5000+"! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "<a[a-zA-Z0-9 =\"\'.:;?]*(href=[\\\"\\\'](http:\\/\\/|\\.\\/|\\/)?\\w+(\\.\\w+)*(\\/\\w+(\\.\\w+)?)*(\\/|\\?\\w*=\\w*(&\\w*=\\w*)*)?[\\\"\\\'])*(>[a-zA-Z0-9 =\"\'<>.:;?]*</a>)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<a");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("href=\"0\"");
            }
            // 后缀
            attackString.append("! _1_POA(i)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
