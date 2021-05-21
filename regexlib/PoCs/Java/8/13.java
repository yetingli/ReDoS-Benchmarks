//vuln pattern: POA
//vuln degree: POL
//mul vuln: N
//vuln location: \s*[+-]?\s*

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Demo {

    public static void main(String[] args) throws InterruptedException {
        String regex = "^\\s*[+-]?\\s*(?:\\d{1,3}(?:(,?)\\d{3})?(?:\\1\\d{3})*(\\.\\d*)?|\\.\\d+)\\s*$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i*10000 ; j++) {
                attackString.append(" ");
            }
            // 后缀
            attackString.append("!");
            long time1 = System.nanoTime();
            Matcher matcher = Pattern.compile(regex).matcher(attackString);
            boolean isMatch = matcher.find();
//            boolean isMatch = Pattern.matches(regex, attackString);
            long time2 = System.nanoTime();
            System.out.println(attackString.length() + " " + isMatch + " "+ (time2 - time1)/1e9+"s");

        }
    }







}
