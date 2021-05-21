import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8292 {
    /* 8292
     * ^((https|http)://)?(www.)?(([a-zA-Z0-9\-]{2,})\.)+([a-zA-Z0-9\-]{2,4})(/[\w\.]{0,})*((\?)(([\w\%]{0,}=[\w\%]{0,}&?)|[\w]{0,})*)?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"aa.aa?"+"w="*16+"! _1_EOD(i4)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((https|http)://)?(www.)?(([a-zA-Z0-9\\-]{2,})\\.)+([a-zA-Z0-9\\-]{2,4})(/[\\w\\.]{0,})*((\\?)(([\\w\\%]{0,}=[\\w\\%]{0,}&?)|[\\w]{0,})*)?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("aa.aa?");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("w=");
            }
            // 后缀
            attackString.append("! _1_EOD(i4)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
