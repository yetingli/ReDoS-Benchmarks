import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1327 {
    /* 1327
     * ^(?:(?:[^@,"\[\]\x5c\x00-\x20\x7f-\xff\.]|\x5c(?=[@,"\[\]\x5c\x00-\x20\x7f-\xff]))(?:[^@,"\[\]\x5c\x00-\x20\x7f-\xff\.]|(?<=\x5c)[@,"\[\]\x5c\x00-\x20\x7f-\xff]|\x5c(?=[@,"\[\]\x5c\x00-\x20\x7f-\xff])|\.(?=[^\.])){1,62}(?:[^@,"\[\]\x5c\x00-\x20\x7f-\xff\.]|(?<=\x5c)[@,"\[\]\x5c\x00-\x20\x7f-\xff])|"(?:[^"]|(?<=\x5c)"){1,62}")@(?:(?:[a-z0-9][a-z0-9-]{1,61}[a-z0-9]\.?)+\.[a-z]{2,6}|\[(?:[0-1]?\d?\d|2[0-4]\d|25[0-5])(?:\.(?:[0-1]?\d?\d|2[0-4]\d|25[0-5])){3}\])$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"::"+"\\"*32+"@1 __EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?:(?:[^@,\"\\[\\]\\x5c\\x00-\\x20\\x7f-\\xff\\.]|\\x5c(?=[@,\"\\[\\]\\x5c\\x00-\\x20\\x7f-\\xff]))(?:[^@,\"\\[\\]\\x5c\\x00-\\x20\\x7f-\\xff\\.]|(?<=\\x5c)[@,\"\\[\\]\\x5c\\x00-\\x20\\x7f-\\xff]|\\x5c(?=[@,\"\\[\\]\\x5c\\x00-\\x20\\x7f-\\xff])|\\.(?=[^\\.])){1,62}(?:[^@,\"\\[\\]\\x5c\\x00-\\x20\\x7f-\\xff\\.]|(?<=\\x5c)[@,\"\\[\\]\\x5c\\x00-\\x20\\x7f-\\xff])|\"(?:[^\"]|(?<=\\x5c)\"){1,62}\")@(?:(?:[a-z0-9][a-z0-9-]{1,61}[a-z0-9]\\.?)+\\.[a-z]{2,6}|\\[(?:[0-1]?\\d?\\d|2[0-4]\\d|25[0-5])(?:\\.(?:[0-1]?\\d?\\d|2[0-4]\\d|25[0-5])){3}\\])$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("::");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\\");
            }
            // 后缀
            attackString.append("@1 __EOA(iii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
