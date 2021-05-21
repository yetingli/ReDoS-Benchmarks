import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_7214 {
    /* 7214
     * </?(a|abbr|acronym|address|applet|area|b|base|basefont|bdo|big|blockquote|body|br|button|caption|center|cite|code|col|colgroup|dd|del|dir|div|dfn|dl|dt|em|fieldset|font|form|frame|frameset|h[1-6]|head|hr|html|i|iframe|img|input|ins|isindex|kbd|label|legend|li|link|map|menu|meta|noframes|noscript|object|ol|optgroup|option|p|param|pre|q|s|samp|script|select|small|span|strike|strong|style|sub|sup|table|tbody|td|textarea|tfoot|th|thead|title|tr|tt|u|ul|var|xmp)\b((\"[^\"]*\"|\'[^\']*\')*|[^\"\'>])*>
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"""<a"+"'"*64+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "</?(a|abbr|acronym|address|applet|area|b|base|basefont|bdo|big|blockquote|body|br|button|caption|center|cite|code|col|colgroup|dd|del|dir|div|dfn|dl|dt|em|fieldset|font|form|frame|frameset|h[1-6]|head|hr|html|i|iframe|img|input|ins|isindex|kbd|label|legend|li|link|map|menu|meta|noframes|noscript|object|ol|optgroup|option|p|param|pre|q|s|samp|script|select|small|span|strike|strong|style|sub|sup|table|tbody|td|textarea|tfoot|th|thead|title|tr|tt|u|ul|var|xmp)\\b((\\\"[^\\\"]*\\\"|\\\'[^\\\']*\\\')*|[^\\\"\\\'>])*>";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("\"\"<a");
            // 歧义点
            for (int j = 0; j < i * 1; j++) {
                attackString.append("\'");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
