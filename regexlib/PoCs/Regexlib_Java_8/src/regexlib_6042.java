import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_6042 {
    /* 6042
     * (<\/?)(?i:(?<element>a(bbr|cronym|ddress|pplet|rea)?|b(ase(font)?|do|ig|lockquote|ody|r|utton)?|c(aption|enter|ite|(o(de|l(group)?)))|d(d|el|fn|i(r|v)|l|t)|em|f(ieldset|o(nt|rm)|rame(set)?)|h([1-6]|ead|r|tml)|i(frame|mg|n(put|s)|sindex)?|kbd|l(abel|egend|i(nk)?)|m(ap|e(nu|ta))|no(frames|script)|o(bject|l|pt(group|ion))|p(aram|re)?|q|s(amp|cript|elect|mall|pan|t(r(ike|ong)|yle)|u(b|p))|t(able|body|d|extarea|foot|h|itle|r|t)|u(l)?|var))(\s(?<attr>.+?))*>
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"<a"+" "*32+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(<\\/?)(?i:(?<element>a(bbr|cronym|ddress|pplet|rea)?|b(ase(font)?|do|ig|lockquote|ody|r|utton)?|c(aption|enter|ite|(o(de|l(group)?)))|d(d|el|fn|i(r|v)|l|t)|em|f(ieldset|o(nt|rm)|rame(set)?)|h([1-6]|ead|r|tml)|i(frame|mg|n(put|s)|sindex)?|kbd|l(abel|egend|i(nk)?)|m(ap|e(nu|ta))|no(frames|script)|o(bject|l|pt(group|ion))|p(aram|re)?|q|s(amp|cript|elect|mall|pan|t(r(ike|ong)|yle)|u(b|p))|t(able|body|d|extarea|foot|h|itle|r|t)|u(l)?|var))(\\s(?<attr>.+?))*>";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append(" ");
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
