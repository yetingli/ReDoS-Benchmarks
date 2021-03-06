import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1959 {
    /* 1959
     * ^((http|https|ftp|ftps)+(:\/\/))?(www\.)?(([a-z0-9\.-]{2,})\.(ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|fx|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|aero|asia|cat|coop|edu|gov|jobs|mil|mobi|museum|tel|travel|pro|post|biz|com|info|int|name|net|org|pro|arpa)|((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])))(:([1-9][0-9]?[0-9]?[0-9]?|[1-5][0-9][0-9][0-9][0-9]|6[0-4][0-9][0-9][0-9]|65[0-4][0-9][0-9]|655[0-2][0-9]|6553[0-5]|))?(((\/(([a-zA-Z0-9_\-\%\~\+\&\;]{1,})+)*)*)|\/$)?(\.(php|html|htm|zip$|arj$|rar$|sit$|pdf$|gif$|jpg$|jpeg$|jpe$|tif$|tiff$))?(\?([a-zA-Z0-9_\-]+\=[a-z-A-Z0-9_\-\%\~\+]+)?(\&([a-zA-Z0-9_\-]+\=[a-z-A-Z0-9_\-\%\~\+]+))*)?(\=\?([a-zA-Z0-9_\-])*)?(((\+([a-zA-Z0-9_])*)?(\-([a-zA-Z0-9_])*)?)*)?(\#([a-z-A-Z0-9_\-\%\~\+\&\;]*$))?$
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:"aa.ac"+"+0-"*32+"! _1_EOA(i or ii)"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "^((http|https|ftp|ftps)+(:\\/\\/))?(www\\.)?(([a-z0-9\\.-]{2,})\\.(ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|fx|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|aero|asia|cat|coop|edu|gov|jobs|mil|mobi|museum|tel|travel|pro|post|biz|com|info|int|name|net|org|pro|arpa)|((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])))(:([1-9][0-9]?[0-9]?[0-9]?|[1-5][0-9][0-9][0-9][0-9]|6[0-4][0-9][0-9][0-9]|65[0-4][0-9][0-9]|655[0-2][0-9]|6553[0-5]|))?(((\\/(([a-zA-Z0-9_\\-\\%\\~\\+\\&\\;]{1,})+)*)*)|\\/$)?(\\.(php|html|htm|zip$|arj$|rar$|sit$|pdf$|gif$|jpg$|jpeg$|jpe$|tif$|tiff$))?(\\?([a-zA-Z0-9_\\-]+\\=[a-z-A-Z0-9_\\-\\%\\~\\+]+)?(\\&([a-zA-Z0-9_\\-]+\\=[a-z-A-Z0-9_\\-\\%\\~\\+]+))*)?(\\=\\?([a-zA-Z0-9_\\-])*)?(((\\+([a-zA-Z0-9_])*)?(\\-([a-zA-Z0-9_])*)?)*)?(\\#([a-z-A-Z0-9_\\-\\%\\~\\+\\&\\;]*$))?$";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // ??????
            attackString.append("aa.ac");
            // ?????????
            for (int j = 0; j < i * 1; j++) {
                attackString.append("+0-");
            }
            // ??????
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
