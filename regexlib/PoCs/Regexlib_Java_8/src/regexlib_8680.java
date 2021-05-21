import java.util.regex.Pattern;

public class regexlib_8680 {

    public static void main(String[] args) throws InterruptedException {
        String regex = "(((ht|f)tp(s?))\\://)?(\\bw{3}[^w]\\b)?[^w{4}][^\\@]([0-9a-zA-Z\\-]+\\.)+[a-zA-Z]{2,6}(\\:[0-9]+)?(/\\S*)?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // ""+"--"*5000+"!1 _SLQ_2!@ \n_1"
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("--");
            }
            // 后缀
            attackString.append("!1 _SLQ_2!@ \\n_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
