import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3422 {
    /* 3422
     * (?:Provider="??(?<Provider>[^;\n]+)"??[;\n"]??|Data\sSource=(?<DataSource>[^;\n]+)[;\n"]??|Initial\sCatalog=(?<InitialCatalog>[^;\n]+)[;\n"]??|User\sID=(?<UserID>[^;\n]+)[;\n"]??|Password="??(?<Password>[^;\n]+)"??[;\n"]??|Integrated\sSecurity=(?<IntegratedSecurity>[^;\n]+)[;\n]??|Connection\sTimeOut=(?<ConnectionTimeOut>[^;\n]+)[;\n"]??)+$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"Provider=" ";"*16+"! _1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:Provider=\"??(?<Provider>[^;\\n]+)\"??[;\\n\"]??|Data\\sSource=(?<DataSource>[^;\\n]+)[;\\n\"]??|Initial\\sCatalog=(?<InitialCatalog>[^;\\n]+)[;\\n\"]??|User\\sID=(?<UserID>[^;\\n]+)[;\\n\"]??|Password=\"??(?<Password>[^;\\n]+)\"??[;\\n\"]??|Integrated\\sSecurity=(?<IntegratedSecurity>[^;\\n]+)[;\\n]??|Connection\\sTimeOut=(?<ConnectionTimeOut>[^;\\n]+)[;\\n\"]??)+$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("Provider=\" \";");
            }
            // 后缀
            attackString.append("! _1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
