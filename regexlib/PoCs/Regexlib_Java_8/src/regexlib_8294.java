import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8294 {
    /* 8294
     * ^(sip|sips):.*\@((\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})|([a-zA-Z\-\.]+\.[a-zA-Z]{2,5}))(:[\d]{1,5})?([\w\-?\@?\;?\,?\=\%\&]+)?
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"sip:@11"+"0000"*80000+"! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(sip|sips):.*\\@((\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3})|([a-zA-Z\\-\\.]+\\.[a-zA-Z]{2,5}))(:[\\d]{1,5})?([\\w\\-?\\@?\\;?\\,?\\=\\%\\&]+)?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("sip:@11");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("0000");
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
