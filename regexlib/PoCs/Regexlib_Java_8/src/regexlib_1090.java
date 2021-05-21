import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1090 {
    /* 1090
     * (?:(?:[a-zA-Z0-9/;\?&=:\-_\$\+!\*'\(\|\\~\[\]#%\.](?!www))+(?:\.[Cc]om|\.[Ee]du|\.[gG]ov|\.[Ii]nt|\.[Mm]il|\.[Nn]et|\.[Oo]rg|\.[Bb]iz|\.[Ii]nfo|\.[Nn]ame|\.[Pp]ro|\.[Aa]ero|\.[cC]oop|\.[mM]useum|\.[Cc]at|\.[Jj]obs|\.[Tt]ravel|\.[Aa]rpa|\.[Mm]obi|\.[Aa]c|\.[Aa]d|\.[aA]e|\.[aA]f|\.[aA]g|\.[aA]i|\.[aA]l|\.[aA]m|\.[aA]n|\.[aA]o|\.[aA]q|\.[aA]r|\.[aA]s|\.[aA]t|\.[aA]u|\.[aA]w|\.[aA]z|\.[aA]x|\.[bB]a|\.[bB]b|\.[bB]d|\.[bB]e|\.[bB]f|\.[bB]g|\.[bB]h|\.[bB]i|\.[bB]j|\.[bB]m|\.[bB]n|\.[bB]o|\.[bB]r|\.[bB]s|\.[bB]t|\.[bB]v|\.[bB]w|\.[bB]y|\.[bB]z|\.[cC]a|\.[cC]c|\.[cC]d|\.[cC]f|\.[cC]g|\.[cC]h|\.[cC]i|\.[cC]k|\.[cC]l|\.[cC]m|\.[cC]n|\.[cC]o|\.[cC]r|\.[cC]s|\.[cC]u|\.[cC]v|\.[cC]x|\.[cC]y|\.[cC]z|\.[dD]e|\.[dD]j|\.[dD]k|\.[dD]m|\.[dD]o|\.[dD]z|\.[eE]c|\.[eE]e|\.[eE]g|\.[eE]h|\.[eE]r|\.[eE]s|\.[eE]t|\.[eE]u|\.[fF]i|\.[fF]j|\.[fF]k|\.[fF]m|\.[fF]o|\.[fF]r|\.[gG]a|\.[gG]b|\.[gG]d|\.[gG]e|\.[gG]f|\.[gG]g|\.[gG]h|\.[gG]i|\.[gG]l|\.[gG]m|\.[gG]n|\.[gG]p|\.[gG]q|\.[gG]r|\.[gG]s|\.[gG]t|\.[gG]u|\.[gG]w|\.[gG]y|\.[hH]k|\.[hH]m|\.[hH]n|\.[hH]r|\.[hH]t|\.[hH]u|\.[iI]d|\.[iI]e|\.[iI]l|\.[iI]m|\.[iI]n|\.[iI]o|\.[iI]q|\.[iI]r|\.[iI]s|\.[iI]t|\.[jJ]e|\.[jJ]m|\.[jJ]o|\.[jJ]p|\.[kK]e|\.[kK]g|\.[kK]h|\.[kK]i|\.[kK]m|\.[kK]n|\.[kK]p|\.[kK]r|\.[kK]w|\.[kK]y|\.[kK]z|\.[lL]a|\.[lL]b|\.[lL]c|\.[lL]i|\.[lL]k|\.[lL]r|\.[lL]s|\.[lL]t|\.[lL]u|\.[lL]v|\.[lL]y|\.[mM]a|\.[mM]c|\.[mM]d|\.[mM]g|\.[mM]h|\.[mM]k|\.[mM]l|\.[mM]m|\.[mM]n|\.[mM]o|\.[mM]p|\.[mM]q|\.[mM]r|\.[mM]s|\.[mM]t|\.[mM]u|\.[mM]v|\.[mM]w|\.[mM]x|\.[mM]y|\.[mM]z|\.[nN]a|\.[nN]c|\.[nN]e|\.[nN]f|\.[nN]g|\.[nN]i|\.[nN]l|\.[nN]o|\.[nN]p|\.[nN]r|\.[nN]u|\.[nN]z|\.[oO]m|\.[pP]a|\.[pP]e|\.[pP]f|\.[pP]g|\.[pP]h|\.[pP]k|\.[pP]l|\.[pP]m|\.[pP]n|\.[pP]r|\.[pP]s|\.[pP]t|\.[pP]w|\.[pP]y|\.[qP]a|\.[rR]e|\.[rR]o|\.[rR]u|\.[rR]w|\.[sS]a|\.[sS]b|\.[sS]c|\.[sS]d|\.[sS]e|\.[sS]g|\.[sS]h|\.[Ss]i|\.[sS]j|\.[sS]k|\.[sS]l|\.[sS]m|\.[sS]n|\.[sS]o|\.[sS]r|\.[sS]t|\.[sS]v|\.[sS]y|\.[sS]z|\.[tT]c|\.[tT]d|\.[tT]f|\.[tT]g|\.[tT]h|\.[tT]j|\.[tT]k|\.[tT]l|\.[tT]m|\.[tT]n|\.[tT]o|\.[tT]p|\.[tT]r|\.[tT]t|\.[tT]v|\.[tT]w|\.[tT]z|\.[uU]a|\.[uU]g|\.[uU]k|\.[uU]m|\.[uU]s|\.[uU]y|\.[uU]z|\.[vV]a|\.[vV]c|\.[vV]e|\.[vV]g|\.[vV]i|\.[vV]n|\.[vV]u|\.[wW]f|\.[wW]s|\.[yY]e|\.[yY]t|\.[yY]u|\.[zZ]a|\.[zZ]m|\.[zZ]w))
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"a!www"*80000+"◎@! _1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:(?:[a-zA-Z0-9/;\\?&=:\\-_\\$\\+!\\*\'\\(\\|\\\\~\\[\\]#%\\.](?!www))+(?:\\.[Cc]om|\\.[Ee]du|\\.[gG]ov|\\.[Ii]nt|\\.[Mm]il|\\.[Nn]et|\\.[Oo]rg|\\.[Bb]iz|\\.[Ii]nfo|\\.[Nn]ame|\\.[Pp]ro|\\.[Aa]ero|\\.[cC]oop|\\.[mM]useum|\\.[Cc]at|\\.[Jj]obs|\\.[Tt]ravel|\\.[Aa]rpa|\\.[Mm]obi|\\.[Aa]c|\\.[Aa]d|\\.[aA]e|\\.[aA]f|\\.[aA]g|\\.[aA]i|\\.[aA]l|\\.[aA]m|\\.[aA]n|\\.[aA]o|\\.[aA]q|\\.[aA]r|\\.[aA]s|\\.[aA]t|\\.[aA]u|\\.[aA]w|\\.[aA]z|\\.[aA]x|\\.[bB]a|\\.[bB]b|\\.[bB]d|\\.[bB]e|\\.[bB]f|\\.[bB]g|\\.[bB]h|\\.[bB]i|\\.[bB]j|\\.[bB]m|\\.[bB]n|\\.[bB]o|\\.[bB]r|\\.[bB]s|\\.[bB]t|\\.[bB]v|\\.[bB]w|\\.[bB]y|\\.[bB]z|\\.[cC]a|\\.[cC]c|\\.[cC]d|\\.[cC]f|\\.[cC]g|\\.[cC]h|\\.[cC]i|\\.[cC]k|\\.[cC]l|\\.[cC]m|\\.[cC]n|\\.[cC]o|\\.[cC]r|\\.[cC]s|\\.[cC]u|\\.[cC]v|\\.[cC]x|\\.[cC]y|\\.[cC]z|\\.[dD]e|\\.[dD]j|\\.[dD]k|\\.[dD]m|\\.[dD]o|\\.[dD]z|\\.[eE]c|\\.[eE]e|\\.[eE]g|\\.[eE]h|\\.[eE]r|\\.[eE]s|\\.[eE]t|\\.[eE]u|\\.[fF]i|\\.[fF]j|\\.[fF]k|\\.[fF]m|\\.[fF]o|\\.[fF]r|\\.[gG]a|\\.[gG]b|\\.[gG]d|\\.[gG]e|\\.[gG]f|\\.[gG]g|\\.[gG]h|\\.[gG]i|\\.[gG]l|\\.[gG]m|\\.[gG]n|\\.[gG]p|\\.[gG]q|\\.[gG]r|\\.[gG]s|\\.[gG]t|\\.[gG]u|\\.[gG]w|\\.[gG]y|\\.[hH]k|\\.[hH]m|\\.[hH]n|\\.[hH]r|\\.[hH]t|\\.[hH]u|\\.[iI]d|\\.[iI]e|\\.[iI]l|\\.[iI]m|\\.[iI]n|\\.[iI]o|\\.[iI]q|\\.[iI]r|\\.[iI]s|\\.[iI]t|\\.[jJ]e|\\.[jJ]m|\\.[jJ]o|\\.[jJ]p|\\.[kK]e|\\.[kK]g|\\.[kK]h|\\.[kK]i|\\.[kK]m|\\.[kK]n|\\.[kK]p|\\.[kK]r|\\.[kK]w|\\.[kK]y|\\.[kK]z|\\.[lL]a|\\.[lL]b|\\.[lL]c|\\.[lL]i|\\.[lL]k|\\.[lL]r|\\.[lL]s|\\.[lL]t|\\.[lL]u|\\.[lL]v|\\.[lL]y|\\.[mM]a|\\.[mM]c|\\.[mM]d|\\.[mM]g|\\.[mM]h|\\.[mM]k|\\.[mM]l|\\.[mM]m|\\.[mM]n|\\.[mM]o|\\.[mM]p|\\.[mM]q|\\.[mM]r|\\.[mM]s|\\.[mM]t|\\.[mM]u|\\.[mM]v|\\.[mM]w|\\.[mM]x|\\.[mM]y|\\.[mM]z|\\.[nN]a|\\.[nN]c|\\.[nN]e|\\.[nN]f|\\.[nN]g|\\.[nN]i|\\.[nN]l|\\.[nN]o|\\.[nN]p|\\.[nN]r|\\.[nN]u|\\.[nN]z|\\.[oO]m|\\.[pP]a|\\.[pP]e|\\.[pP]f|\\.[pP]g|\\.[pP]h|\\.[pP]k|\\.[pP]l|\\.[pP]m|\\.[pP]n|\\.[pP]r|\\.[pP]s|\\.[pP]t|\\.[pP]w|\\.[pP]y|\\.[qP]a|\\.[rR]e|\\.[rR]o|\\.[rR]u|\\.[rR]w|\\.[sS]a|\\.[sS]b|\\.[sS]c|\\.[sS]d|\\.[sS]e|\\.[sS]g|\\.[sS]h|\\.[Ss]i|\\.[sS]j|\\.[sS]k|\\.[sS]l|\\.[sS]m|\\.[sS]n|\\.[sS]o|\\.[sS]r|\\.[sS]t|\\.[sS]v|\\.[sS]y|\\.[sS]z|\\.[tT]c|\\.[tT]d|\\.[tT]f|\\.[tT]g|\\.[tT]h|\\.[tT]j|\\.[tT]k|\\.[tT]l|\\.[tT]m|\\.[tT]n|\\.[tT]o|\\.[tT]p|\\.[tT]r|\\.[tT]t|\\.[tT]v|\\.[tT]w|\\.[tT]z|\\.[uU]a|\\.[uU]g|\\.[uU]k|\\.[uU]m|\\.[uU]s|\\.[uU]y|\\.[uU]z|\\.[vV]a|\\.[vV]c|\\.[vV]e|\\.[vV]g|\\.[vV]i|\\.[vV]n|\\.[vV]u|\\.[wW]f|\\.[wW]s|\\.[yY]e|\\.[yY]t|\\.[yY]u|\\.[zZ]a|\\.[zZ]m|\\.[zZ]w))";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("a!www");
            }
            // 后缀
            attackString.append("◎@! _1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
