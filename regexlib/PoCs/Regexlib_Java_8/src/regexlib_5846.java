import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5846 {
    /* 5846
     * ((http|ftp|https|ftps):\/\/)?[\w\-_\.]+\.(([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(:[0-9]+)?\/?(([\w\-\.,@^%:/~\+#]*[\w\-\@^%/~\+#])((\?[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)+(&[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)*)?)?
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"1.aaa"+"aa"*32+"! _1_NQ"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((http|ftp|https|ftps):\\/\\/)?[\\w\\-_\\.]+\\.(([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(:[0-9]+)?\\/?(([\\w\\-\\.,@^%:/~\\+#]*[\\w\\-\\@^%/~\\+#])((\\?[a-zA-Z0-9\\[\\]\\-\\._+%\\$#\\=~\',]*=[a-zA-Z0-9\\[\\]\\-\\._+%\\$#\\=~\',]*)+(&[a-zA-Z0-9\\[\\]\\-\\._+%\\$#\\=~\',]*=[a-zA-Z0-9\\[\\]\\-\\._+%\\$#\\=~\',]*)*)?)?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("1.aaa");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("aa");
            }
            // 后缀
            attackString.append("! _1_NQ");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
