import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_245 {
    /* 245
     * ^(http(s?)\:\/\/)?(www.)?(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_\-]+)?)(\.)(([a-zA-Z]{2,})([0-9a-zA-Z]+)?)(\:\d{0,5})?(\/|(\/[A-Za-z]+([a-zA-Z0-9]+)?)+)?(\?[a-zA-Z0-9\\\&\%\_\.\/\-\=\~\*]+)?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"A.aa"+"/AA"*32+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(http(s?)\\:\\/\\/)?(www.)?(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\\.\\_\\-]+)?)(\\.)(([a-zA-Z]{2,})([0-9a-zA-Z]+)?)(\\:\\d{0,5})?(\\/|(\\/[A-Za-z]+([a-zA-Z0-9]+)?)+)?(\\?[a-zA-Z0-9\\\\\\&\\%\\_\\.\\/\\-\\=\\~\\*]+)?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("A.aa");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("/AA");
            }
            // 后缀
            attackString.append("! _1_EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
