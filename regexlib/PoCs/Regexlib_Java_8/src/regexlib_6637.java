import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_6637 {
    /* 6637
     * [p|P][\s]*[o|O][\s]*[b|B][\s]*[o|O][\s]*[x|X][\s]*[a-zA-Z0-9]*|\b[P|p]+(OST|ost|o|O)?\.?\s*[O|o|0]+(ffice|FFICE)?\.?\s*[B|b][O|o|0]?[X|x]+\.?\s+[#]?(\d+)*(\D+)*\b
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"POBX "+"1"*32+"!1 __NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "[p|P][\\s]*[o|O][\\s]*[b|B][\\s]*[o|O][\\s]*[x|X][\\s]*[a-zA-Z0-9]*|\\b[P|p]+(OST|ost|o|O)?\\.?\\s*[O|o|0]+(ffice|FFICE)?\\.?\\s*[B|b][O|o|0]?[X|x]+\\.?\\s+[#]?(\\d+)*(\\D+)*\\b";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("POBX ");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("1");
            }
            // 后缀
            attackString.append("!1 __NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
