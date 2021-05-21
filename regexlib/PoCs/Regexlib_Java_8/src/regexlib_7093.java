import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7093 {
    /* 7093
     * ^(?<Namespace>(?:[\w][\w\d]*\.?)*)\.(?<Class>[\w][\w\d<>]*(?:(?:\+[\w][\w\d<>]*)+|))(?:|,\W?(?<Assembly>(?<AssemblyName>[^\W/\\:*?"<>|]+)(?:$|(?:,\W?(?:(?<Version>Version=(?<VersionValue>(?:\d{1,2}\.?){1,4}))|(?<Culture>Culture=(?<CultureValue>neutral|\w{2}-\w{2}))|(?<PublicKeyToken>PublicKeyToken=(?<PublicKeyTokenValue>[A-Fa-f0-9]{16})))(?:,\W?)?){3})))$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"0"*32+"!1 __EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^(?<Namespace>(?:[\\w][\\w\\d]*\\.?)*)\\.(?<Class>[\\w][\\w\\d<>]*(?:(?:\\+[\\w][\\w\\d<>]*)+|))(?:|,\\W?(?<Assembly>(?<AssemblyName>[^\\W/\\\\:*?\"<>|]+)(?:$|(?:,\\W?(?:(?<Version>Version=(?<VersionValue>(?:\\d{1,2}\\.?){1,4}))|(?<Culture>Culture=(?<CultureValue>neutral|\\w{2}-\\w{2}))|(?<PublicKeyToken>PublicKeyToken=(?<PublicKeyTokenValue>[A-Fa-f0-9]{16})))(?:,\\W?)?){3})))$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("0");
            }
            // 后缀
            attackString.append("!1 __EOA(iii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
