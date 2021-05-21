import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_6839 {
    /* 6839
     * <ul>\n<li>(?<type>document_name|url)=(?<doc>.*?)<li>.*?<ul>\n(?:<li>(?<propName>.*?)\n<li>(?<propValue>.*?))+</ul>\n</ul>
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"<ul>\n<li>document_name=<li>"*5000+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "<ul>\\n<li>(?<type>document_name|url)=(?<doc>.*?)<li>.*?<ul>\\n(?:<li>(?<propName>.*?)\\n<li>(?<propValue>.*?))+</ul>\\n</ul>";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("<ul>\n<li>document_name=<li>");
            }
            // 后缀
            attackString.append("! _1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
