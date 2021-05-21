import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_8355 {
    /* 8355
     * ([\w\-\.]*)@(([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})|([\w\-]+\.)+(((af|ax|al|dz|as|ad|ao|ai|aq|ag|am|aw|au|at|az|bs|bh|bd|bb|by|be|bz|bj|bm|bt|bo|ba|bw|bv|br|io|bn|bg|bf|kh|cm|ca|cv|ky|cf|td|cl|cn|cx|cc|km|cg|cd|ck|cr|ci|hr|cu|cy|cz|dk|dj|dm|do|ec|eg|sv|gq|er|ee|et|fk|fo|fj|fi|fr|gf|pf|tf|ga|gm|ge|de|gh|gi|gr|gl|gd|gp|gu|gt| gg|gn|gw|gy|ht|hm|va|hn|hk|hu|is|id|ir|iq|ie|im|il|it|jm|jp|je|jo|kz|ke|ki|kp|kr|kw|kg|la|lv|lb|ls|lr|ly|li|lt|lu|mo|mk|mg|mw|my|mv|ml|mt|mh|mq|mr|yt|mx|fm|md|mc|mn|ms|ma|mz|mm|nr|np|nl|an|nc|nz|ni|ng|nu|nf|mp|no|om|pk|pw|ps|pa|pg|py|pe|ph|pn|pl|pt|qa|re|ro|ru|rw|sh|kn|lc|pm|vc|ws|sm|st|sa|sn|cs|sc|sl|sg|sk|si|sb|so|za|gs|es|lk|sd|sr|sj|sz|se|ch|sy|tw|tj|tz|th|tl|tg|tk|to|tt|tn|tr|tm|tc|tv|ug|ua|gb|us|um|uy|uz|vu|ve|vn|vg|vi|wf|eh|ye|zm|zw|uk|com|edu|gov|int|mil|net|org|biz|info|name|pro|aero|coop|museum|arpa|co|in|ne|bi|na|pr|ae|mu|ar)))?)
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"1"*10000+"! _1SLQ_1"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "([\\w\\-\\.]*)@(([\\d]{1,3}\\.[\\d]{1,3}\\.[\\d]{1,3}\\.[\\d]{1,3})|([\\w\\-]+\\.)+(((af|ax|al|dz|as|ad|ao|ai|aq|ag|am|aw|au|at|az|bs|bh|bd|bb|by|be|bz|bj|bm|bt|bo|ba|bw|bv|br|io|bn|bg|bf|kh|cm|ca|cv|ky|cf|td|cl|cn|cx|cc|km|cg|cd|ck|cr|ci|hr|cu|cy|cz|dk|dj|dm|do|ec|eg|sv|gq|er|ee|et|fk|fo|fj|fi|fr|gf|pf|tf|ga|gm|ge|de|gh|gi|gr|gl|gd|gp|gu|gt| gg|gn|gw|gy|ht|hm|va|hn|hk|hu|is|id|ir|iq|ie|im|il|it|jm|jp|je|jo|kz|ke|ki|kp|kr|kw|kg|la|lv|lb|ls|lr|ly|li|lt|lu|mo|mk|mg|mw|my|mv|ml|mt|mh|mq|mr|yt|mx|fm|md|mc|mn|ms|ma|mz|mm|nr|np|nl|an|nc|nz|ni|ng|nu|nf|mp|no|om|pk|pw|ps|pa|pg|py|pe|ph|pn|pl|pt|qa|re|ro|ru|rw|sh|kn|lc|pm|vc|ws|sm|st|sa|sn|cs|sc|sl|sg|sk|si|sb|so|za|gs|es|lk|sd|sr|sj|sz|se|ch|sy|tw|tj|tz|th|tl|tg|tk|to|tt|tn|tr|tm|tc|tv|ug|ua|gb|us|um|uy|uz|vu|ve|vn|vg|vi|wf|eh|ye|zm|zw|uk|com|edu|gov|int|mil|net|org|biz|info|name|pro|aero|coop|museum|arpa|co|in|ne|bi|na|pr|ae|mu|ar)))?)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("1");
            }
            // 后缀
            attackString.append("! _1SLQ_1");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
