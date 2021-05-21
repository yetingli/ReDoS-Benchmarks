import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1712 {
    /* 1712
     * (\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*(\s)*(\()(\s)*((int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*((\s)*[,](\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*)*)?(\s)*(\))(\s)*;
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"int"+"\t"*5000+"◎@! _1!_1!1 _!1 _!_1◎@! _1!_1! _1!_1◎@! _1!_1! _1!_1!\n_SLQ_3"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(\\s)*(int|void|float|char|double|string)((\\s)|(\\*))*(\\&?)(\\s)+([a-z])([a-z0-9])*(\\s)*(\\()(\\s)*((int|void|float|char|double|string)((\\s)|(\\*))*(\\&?)(\\s)+([a-z])([a-z0-9])*((\\s)*[,](\\s)*(int|void|float|char|double|string)((\\s)|(\\*))*(\\&?)(\\s)+([a-z])([a-z0-9])*)*)?(\\s)*(\\))(\\s)*;";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("int");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("\t");
            }
            // 后缀
            attackString.append("◎@! _1!_1!1 _!1 _!_1◎@! _1!_1! _1!_1◎@! _1!_1! _1!_1!\n_SLQ_3");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
