import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1613 {
    /* 1613
     * ^((http|HTTP|https|HTTPS|ftp|FTP?)\:\/\/)?((www|WWW)+\.)+(([0-9]{1,3}){3}[0-9]{1,3}\.|([\w!~*'()-]+\.)*([\w^-][\w-]{0,61})?[\w]\.[a-z]{2,6})(:[0-9]{1,4})?((\/*)|(\/+[\w!~*'().;?:@&=+$,%#-]+)+\/*)$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"WWW."*5000+"! _1_POA(i)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((http|HTTP|https|HTTPS|ftp|FTP?)\\:\\/\\/)?((www|WWW)+\\.)+(([0-9]{1,3}){3}[0-9]{1,3}\\.|([\\w!~*\'()-]+\\.)*([\\w^-][\\w-]{0,61})?[\\w]\\.[a-z]{2,6})(:[0-9]{1,4})?((\\/*)|(\\/+[\\w!~*\'().;?:@&=+$,%#-]+)+\\/*)$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("WWW.");
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
