import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3817 {
    /* 3817
     * ^(https?|ftp)(:\/\/)(([\w]{3,}\.[\w]+\.[\w]{2,6})|([\d]{3}\.[\d]{1,3}\.[\d]{3}\.[\d]{1,3}))(\:[0,9]+)*(\/?$|((\/[\w\W]+)+\.[\w]{3,4})?$)
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"http://111.1.11"+"/"*32+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(https?|ftp)(:\\/\\/)(([\\w]{3,}\\.[\\w]+\\.[\\w]{2,6})|([\\d]{3}\\.[\\d]{1,3}\\.[\\d]{3}\\.[\\d]{1,3}))(\\:[0,9]+)*(\\/?$|((\\/[\\w\\W]+)+\\.[\\w]{3,4})?$)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http://111.1.11");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("/");
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
