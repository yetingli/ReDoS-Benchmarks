import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_2403 {
    /* 2403
     * actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=(.*)&pass=(.*)&new_lang=pt_BR&select_view=imp
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=&pass="*256+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=(.*)&pass=(.*)&new_lang=pt_BR&select_view=imp";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=&pass=");
            }
            // 后缀
            attackString.append("! _1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
