import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2766 {
    /* 2766
     * (?:@[A-Z]\w*\s+)*(?:(?:public|private|protected)\s+)?(?:(?:(?:abstract|final|native|transient|static|synchronized)\s+)*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>\s+)?(?:(?:(?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\]))*)|void)+)\s+(([a-zA-Z]\w*)\s*\(\s*(((?:[A-Z]\w*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>)?|int|float|double|char|boolean|byte|long|short)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*)(?:,\s*((?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*))*)?\s*\))
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"A"*32+"! _1_EOA(iii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:@[A-Z]\\w*\\s+)*(?:(?:public|private|protected)\\s+)?(?:(?:(?:abstract|final|native|transient|static|synchronized)\\s+)*(?:<(?:\\?|[A-Z]\\w*)(?:\\s+(?:extends|super)\\s+[A-Z]\\w*)?(?:(?:,\\s*(?:\\?|[A-Z]\\w*))(?:\\s+(?:extends|super)\\s+[A-Z]\\w*)?)*>\\s+)?(?:(?:(?:[A-Z]\\w*(?:<[A-Z]\\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\\[\\]))*)|void)+)\\s+(([a-zA-Z]\\w*)\\s*\\(\\s*(((?:[A-Z]\\w*(?:<(?:\\?|[A-Z]\\w*)(?:\\s+(?:extends|super)\\s+[A-Z]\\w*)?(?:(?:,\\s*(?:\\?|[A-Z]\\w*))(?:\\s+(?:extends|super)\\s+[A-Z]\\w*)?)*>)?|int|float|double|char|boolean|byte|long|short)(?:(?:\\[\\])|\\.\\.\\.)?\\s+[a-z]\\w*)(?:,\\s*((?:[A-Z]\\w*(?:<[A-Z]\\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\\[\\])|\\.\\.\\.)?\\s+[a-z]\\w*))*)?\\s*\\))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("A");
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
