import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1550 {
    /* 1550
     * ((?!(This|It|He|She|[MTWFS][a-z]+day|[JF][a-z]+ary|March|April|May|June|July|August|[SOND][a-z]+ber))(?:[A-Z]+\.\s?)*(?:(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+)(?:(\b\s?((?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+|[A-Z]+\.|on|of|the|von|der|van|de|bin|and))*(?:\s*(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+))?)
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"Aa"+"AA"*128+"! _1_EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((?!(This|It|He|She|[MTWFS][a-z]+day|[JF][a-z]+ary|March|April|May|June|July|August|[SOND][a-z]+ber))(?:[A-Z]+\\.\\s?)*(?:(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+)(?:(\\b\\s?((?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+|[A-Z]+\\.|on|of|the|von|der|van|de|bin|and))*(?:\\s*(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+))?)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("Aa");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("AA");
            }
            // 后缀
            attackString.append("! _1_EOA(iii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
