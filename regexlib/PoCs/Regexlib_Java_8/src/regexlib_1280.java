import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1280 {
    /* 1280
     * (((0*[1-9]|[12][0-9]|3[01])([-./])(0*[13578]|10|12)([-./])(\d{4}))|((0*[1-9]|[12][0-9]|30)([-./])(0*[469]|11)([-./])(\d{4}))|((0*[1-9]|1[0-9]|2[0-8])([-./])(02|2)([-./])(\d{4}))|((29)(\.|-|\/)(02|2)([-./])([02468][048]00))|((29)([-./])(02|2)([-./])([13579][26]00))|((29)([-./])(02|2)([-./])([0-9][0-9][0][48]))|((29)([-./])(02|2)([-./])([0-9][0-9][2468][048]))|((29)([-./])(02|2)([-./])([0-9][0-9][13579][26])))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"0"*10000+"!1 _!1 _SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(((0*[1-9]|[12][0-9]|3[01])([-./])(0*[13578]|10|12)([-./])(\\d{4}))|((0*[1-9]|[12][0-9]|30)([-./])(0*[469]|11)([-./])(\\d{4}))|((0*[1-9]|1[0-9]|2[0-8])([-./])(02|2)([-./])(\\d{4}))|((29)(\\.|-|\\/)(02|2)([-./])([02468][048]00))|((29)([-./])(02|2)([-./])([13579][26]00))|((29)([-./])(02|2)([-./])([0-9][0-9][0][48]))|((29)([-./])(02|2)([-./])([0-9][0-9][2468][048]))|((29)([-./])(02|2)([-./])([0-9][0-9][13579][26])))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("0");
            }
            // 后缀
            attackString.append("!1 _!1 _SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
