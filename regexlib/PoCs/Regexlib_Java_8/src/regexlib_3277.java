import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3277 {
    /* 3277
     * (http):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+(\\.[\\w\\-_]+)(\\/)([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?^=%&amp;/~\\+#]+)(\\/)((\\d{8}-)|(\\d{9}-)|(\\d{10}-)|(\\d{11}-))+([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?+html^])?
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"http:\\/\\/\\"+"\\\\"*32+"! _1_EOA(iv)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(http):\\\\/\\\\/[\\\\w\\\\-_]+(\\\\.[\\\\w\\\\-_]+)+(\\\\.[\\\\w\\\\-_]+)(\\\\/)([\\\\w\\\\-\\\\.,@?^=%&amp;:/~\\\\+#]*[\\\\w\\\\-\\\\@?^=%&amp;/~\\\\+#]+)(\\\\/)((\\\\d{8}-)|(\\\\d{9}-)|(\\\\d{10}-)|(\\\\d{11}-))+([\\\\w\\\\-\\\\.,@?^=%&amp;:/~\\\\+#]*[\\\\w\\\\-\\\\@?+html^])?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http:\\/\\/\\");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\\\\");
            }
            // 后缀
            attackString.append("! _1_EOA(iv)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
