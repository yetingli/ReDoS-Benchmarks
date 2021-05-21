import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5840 {
    /* 5840
     * ((http|ftp|https):\/\/w{3}[\d]*.|(http|ftp|https):\/\/|w{3}[\d]*.)([\w\d\._\-#\(\)\[\]\\,;:]+@[\w\d\._\-#\(\)\[\]\\,;:])?([a-z0-9]+.)*[a-z\-0-9]+.([a-z]{2,3})?[a-z]{2,6}(:[0-9]+)?(\/[\/a-z0-9\._\-,]+)*[a-z0-9\-_\.\s\%]+(\?[a-z0-9=%&amp;\.\-,#]+)?
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"http://www1a1aa"+"/"*32+"!1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((http|ftp|https):\\/\\/w{3}[\\d]*.|(http|ftp|https):\\/\\/|w{3}[\\d]*.)([\\w\\d\\._\\-#\\(\\)\\[\\]\\\\,;:]+@[\\w\\d\\._\\-#\\(\\)\\[\\]\\\\,;:])?([a-z0-9]+.)*[a-z\\-0-9]+.([a-z]{2,3})?[a-z]{2,6}(:[0-9]+)?(\\/[\\/a-z0-9\\._\\-,]+)*[a-z0-9\\-_\\.\\s\\%]+(\\?[a-z0-9=%&amp;\\.\\-,#]+)?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("http://www1a1aa");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("/");
            }
            // 后缀
            attackString.append("!1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
