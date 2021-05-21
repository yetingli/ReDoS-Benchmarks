import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_3764 {
    /* 3764
     * (?=^.{1,160}$)^(?:(((?:([a-zA-Z]\:)|(\\{2}[a-zA-Z]\w*)))((?:\\((?:(?![\w\.]*\.(?:gdb|mdb|sde|mdf))[^\\/:*?<>"| .]+[^\\/:*?<>"|]*[^\\/:*?<>"| .]+)))*)(?:\\(([a-zA-Z]\w*)(\.(?:gdb|mdb|sde|mdf))))?)\\?([a-zA-Z]\w*)?(?:\\([a-zA-Z]\w*(?:\.shp)?)(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+\.shp|(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+)(?<!.+\.shp))))$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"a:"+"\\!!!"*16+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?=^.{1,160}$)^(?:(((?:([a-zA-Z]\\:)|(\\\\{2}[a-zA-Z]\\w*)))((?:\\\\((?:(?![\\w\\.]*\\.(?:gdb|mdb|sde|mdf))[^\\\\/:*?<>\"| .]+[^\\\\/:*?<>\"|]*[^\\\\/:*?<>\"| .]+)))*)(?:\\\\(([a-zA-Z]\\w*)(\\.(?:gdb|mdb|sde|mdf))))?)\\\\?([a-zA-Z]\\w*)?(?:\\\\([a-zA-Z]\\w*(?:\\.shp)?)(?<!.+(?:\\.(?:gdb|mdb|sde|mdf)).+\\.shp|(?<!.+(?:\\.(?:gdb|mdb|sde|mdf)).+)(?<!.+\\.shp))))$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("a:");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\\!!!");
            }
            // 后缀
            attackString.append("! _1_EOA(i or ii)");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
