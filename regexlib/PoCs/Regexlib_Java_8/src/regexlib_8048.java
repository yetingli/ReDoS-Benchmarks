import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8048 {
    /* 8048
     * ^(http(s?):\/\/)(www.)?(\w|-)+(\.(\w|-)+)*((\.[a-zA-Z]{2,3})|\.(aero|coop|info|museum|name))+(\/)?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"http://1"+".aero.AA"*1024+"! _1_EOD(i2)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(http(s?):\\/\\/)(www.)?(\\w|-)+(\\.(\\w|-)+)*((\\.[a-zA-Z]{2,3})|\\.(aero|coop|info|museum|name))+(\\/)?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http://1");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(".aero.AA");
            }
            // 后缀
            attackString.append("! _1_EOD(i2)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
