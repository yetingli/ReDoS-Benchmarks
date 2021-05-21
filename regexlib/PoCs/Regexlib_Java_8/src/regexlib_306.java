import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_306 {
    /* 306
     * (?<=(?:\n|:|&|\()\s*?)(Application\.Unlock|Application\.Lock|Application\.Contents\.RemoveAll|Application\.Contents\.Remove|Request\.BinaryRead|Request\.ClientCertificate|Request\.Cookies|Request\.Form|Request\.QueryString|Request\.ServerVariables|Request\.TotalBytes|Response\.AddHeader|Response\.AppendToLog|Response\.BinaryWrite|Response\.Clear|Response\.End|Response\.Flush|Response\.Redirect|Response\.Write|Response\.Buffer|Response\.CacheControl|Response\.Charset|Response\.CodePage|Response\.ContentType|Response\.Cookies|Response\.Expires|Response\.ExpiresAbsolute|Response\.IsClientConnected|Response\.LCID|Response\.PICS|Response\.Status|Server\.ScriptTimeout|Server\.CreateObject|Server\.Execute|Server\.GetLastError|Server\.HTMLEncode|Server\.MapPath|Server\.Transfer|Server\.URLEncode|Session\.Abandon|Session\.Contents\.Remove|Session\.Contents\.RemoveAll|Session\.CodePage|Session\.Contents|Session\.LCID|Session\.SessionID|Session\.StaticObjects|Session\.Timeout|Application|Session|Request)(?=\s|\.|\()
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"<="+"\n"*10000+"!_1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?<=(?:\\n|:|&|\\()\\s*?)(Application\\.Unlock|Application\\.Lock|Application\\.Contents\\.RemoveAll|Application\\.Contents\\.Remove|Request\\.BinaryRead|Request\\.ClientCertificate|Request\\.Cookies|Request\\.Form|Request\\.QueryString|Request\\.ServerVariables|Request\\.TotalBytes|Response\\.AddHeader|Response\\.AppendToLog|Response\\.BinaryWrite|Response\\.Clear|Response\\.End|Response\\.Flush|Response\\.Redirect|Response\\.Write|Response\\.Buffer|Response\\.CacheControl|Response\\.Charset|Response\\.CodePage|Response\\.ContentType|Response\\.Cookies|Response\\.Expires|Response\\.ExpiresAbsolute|Response\\.IsClientConnected|Response\\.LCID|Response\\.PICS|Response\\.Status|Server\\.ScriptTimeout|Server\\.CreateObject|Server\\.Execute|Server\\.GetLastError|Server\\.HTMLEncode|Server\\.MapPath|Server\\.Transfer|Server\\.URLEncode|Session\\.Abandon|Session\\.Contents\\.Remove|Session\\.Contents\\.RemoveAll|Session\\.CodePage|Session\\.Contents|Session\\.LCID|Session\\.SessionID|Session\\.StaticObjects|Session\\.Timeout|Application|Session|Request)(?=\\s|\\.|\\()";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<=");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("\n");
            }
            // 后缀
            attackString.append("!_1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
