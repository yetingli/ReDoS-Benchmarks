
//1165
//^\s*[a-zA-Z0-9,\s]+\s*$
//RESULT-TRUE
//EXPONENT
//nums:1
//EXPONENT	AttackString:""+" "*1024+"!1 _SLQ_1"
//
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1165 {
    public static void main(String[] args) throws InterruptedException {
        String regex = "^\\s*[a-zA-Z0-9,\\s]+\\s*$";
        String prefix_str = "";
        String infix_str = " ";
        String suffix_str = "!1 _SLQ_1";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            attackString.append(prefix_str);
            for (int j = 0; j < i*10000 ; j++) {
                attackString.append(infix_str);
            }
            attackString.append(suffix_str);
            long time1 = System.nanoTime();
            Matcher matcher = Pattern.compile(regex).matcher(attackString);
            boolean isMatch = matcher.find();
//          boolean isMatch = Pattern.matches(regex, attackString);
            long time2 = System.nanoTime();
            System.out.println(attackString.length() + " " + isMatch + " "+ (time2 - time1)/1e9+"s");        }
    }
}
