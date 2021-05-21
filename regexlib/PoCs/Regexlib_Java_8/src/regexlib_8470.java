import java.util.regex.Pattern;

public class regexlib_8470 {

    public static void main(String[] args) throws InterruptedException {
        String regex = "\\b(ht|f)tp[s]?:\\/\\/[^\\s\\n\\r\\t\\<\\>]+(?=[\b\\s\\n\\r\\t\\<])";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("ftp://");
            }
            // 后缀
            attackString.append("");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
