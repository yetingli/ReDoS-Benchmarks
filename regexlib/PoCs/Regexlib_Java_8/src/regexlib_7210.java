import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7210 {
    /* 7210
     * ^[-\w'+*$^&%=~!?{}#|/`]{1}([-\w'+*$^&%=~!?{}#|`.]?[-\w'+*$^&%=~!?{}#|`]{1}){0,31}[-\w'+*$^&%=~!?{}#|`]?@(([a-zA-Z0-9]{1}([-a-zA-Z0-9]?[a-zA-Z0-9]{1}){0,31})\.{1})+([a-zA-Z]{2}|[a-zA-Z]{3}|[a-zA-Z]{4}|[a-zA-Z]{6}){1}$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"-@"+"0"*32+"@1 __EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^[-\\w\'+*$^&%=~!?{}#|/`]{1}([-\\w\'+*$^&%=~!?{}#|`.]?[-\\w\'+*$^&%=~!?{}#|`]{1}){0,31}[-\\w\'+*$^&%=~!?{}#|`]?@(([a-zA-Z0-9]{1}([-a-zA-Z0-9]?[a-zA-Z0-9]{1}){0,31})\\.{1})+([a-zA-Z]{2}|[a-zA-Z]{3}|[a-zA-Z]{4}|[a-zA-Z]{6}){1}$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("-@");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("0");
            }
            // 后缀
            attackString.append("@1 __EOA(iii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
