import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3453 {
    /* 3453
     * (?:(?<protocol>http(?:s?)|ftp)(?:\:\/\/))(?:(?<usrpwd>\w+\:\w+)(?:\@))?(?<domain>[^/\r\n\:]+)?(?<port>\:\d+)?(?<path>(?:\/.*)*\/)?(?<filename>.*?\.(?<ext>\w{2,4}))?(?<qrystr>\??(?:\w+\=[^\#]+)(?:\&?\w+\=\w+)*)*(?<bkmrk>\#.*)?
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"http://"+"/"*32+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:(?<protocol>http(?:s?)|ftp)(?:\\:\\/\\/))(?:(?<usrpwd>\\w+\\:\\w+)(?:\\@))?(?<domain>[^/\\r\\n\\:]+)?(?<port>\\:\\d+)?(?<path>(?:\\/.*)*\\/)?(?<filename>.*?\\.(?<ext>\\w{2,4}))?(?<qrystr>\\??(?:\\w+\\=[^\\#]+)(?:\\&?\\w+\\=\\w+)*)*(?<bkmrk>\\#.*)?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http://");
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
