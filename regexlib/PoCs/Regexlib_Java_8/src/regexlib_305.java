import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_305 {
    /* 305
     * (?<=(?:\n|:|^)\s*?)(if|end\sif|elseif|else|for\seach|for|next|call|class|exit|do|loop|const|dim|erase|option\s(?:explicit|implicit)|(?:public|private|end)\ssub|(?:public|private|end)\sfunction|private|public|redim|select\scase|end\sselect|case\selse|case|set|while|wend|with|end\swith|on\serror\sgoto\s0|on\serror\sresume\snext|exit|end\sclass|property\slet|property\sget|property\sset)(?=\s|$)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"<="+"\n"*5000+"!_1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?<=(?:\\n|:|^)\\s*?)(if|end\\sif|elseif|else|for\\seach|for|next|call|class|exit|do|loop|const|dim|erase|option\\s(?:explicit|implicit)|(?:public|private|end)\\ssub|(?:public|private|end)\\sfunction|private|public|redim|select\\scase|end\\sselect|case\\selse|case|set|while|wend|with|end\\swith|on\\serror\\sgoto\\s0|on\\serror\\sresume\\snext|exit|end\\sclass|property\\slet|property\\sget|property\\sset)(?=\\s|$)";
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
