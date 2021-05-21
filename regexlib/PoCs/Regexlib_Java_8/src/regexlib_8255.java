import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8255 {
    /* 8255
     * ^[\u0600-\u06ff0-9\s]+$|[\u0750-\u077f0-9\s]+$|[\ufb50-\ufc3f0-9\s]+$|[\ufe70-\ufefc0-9\s]+$|[\u06cc0-9\s]+$|[\u067e0-9\s]+$|[\u06af0-9\s]$|[\u06910-9\s]+$|^$
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"ݿ"*10000+"!1 _SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^[\\u0600-\\u06ff0-9\\s]+$|[\\u0750-\\u077f0-9\\s]+$|[\\ufb50-\\ufc3f0-9\\s]+$|[\\ufe70-\\ufefc0-9\\s]+$|[\\u06cc0-9\\s]+$|[\\u067e0-9\\s]+$|[\\u06af0-9\\s]$|[\\u06910-9\\s]+$|^$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("ݿ");
            }
            // 后缀
            attackString.append("!1 _SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
