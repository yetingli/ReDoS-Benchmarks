import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7889 {
    /* 7889
     * (?:(?:(?<=[\s^,(])\*(?=\S)(?!_)(?<bold>.+?)(?<!_)(?<=\S)\*(?=[\s$,.?!]))|(?:(?<=[\s^,(])_(?=\S)(?!\*)(?<underline>.+?)(?<!\*)(?<=\S)_(?=[\s$,.?!]))|(?:(?<=[\s^,(])(?:\*_|_\*)(?=\S)(?<boldunderline>.+?)(?<=\S)(?:\*_|_\*)(?=[\s$,.?!])))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:"<= *=!!_1<!_<=!*= <= _=!!*1<!*<=!_= "+"<= *_=!"*5000+"! _1SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:(?:(?<=[\\s^,(])\\*(?=\\S)(?!_)(?<bold>.+?)(?<!_)(?<=\\S)\\*(?=[\\s$,.?!]))|(?:(?<=[\\s^,(])_(?=\\S)(?!\\*)(?<underline>.+?)(?<!\\*)(?<=\\S)_(?=[\\s$,.?!]))|(?:(?<=[\\s^,(])(?:\\*_|_\\*)(?=\\S)(?<boldunderline>.+?)(?<=\\S)(?:\\*_|_\\*)(?=[\\s$,.?!])))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("<= *=!!_1<!_<=!*= <= _=!!*1<!*<=!_= ");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("<= *_=!");
            }
            // 后缀
            attackString.append("! _1SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
