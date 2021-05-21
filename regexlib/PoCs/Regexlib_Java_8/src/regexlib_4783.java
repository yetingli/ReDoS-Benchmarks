import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_4783 {
    /* 4783
     * (((?<numb1>[\d\.-]+)([\s]*?)(?<oper1>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)){0,1})(?<varname>(salary|mph|kph|ph){1})((([\s]*?)(?<oper2>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)(?<numb2>[\d\.-]+)){0,1})
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"1"*5000+"!1 _!1 _! _1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(((?<numb1>[\\d\\.-]+)([\\s]*?)(?<oper1>(\\>=|\\<=|=\\>|=\\<|\\<|\\>|=){1})([\\s]*?)){0,1})(?<varname>(salary|mph|kph|ph){1})((([\\s]*?)(?<oper2>(\\>=|\\<=|=\\>|=\\<|\\<|\\>|=){1})([\\s]*?)(?<numb2>[\\d\\.-]+)){0,1})";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("1");
            }
            // 后缀
            attackString.append("!1 _!1 _! _1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
