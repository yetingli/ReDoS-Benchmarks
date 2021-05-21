import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5490 {
    /* 5490
     * (LOC[^']*')(GID[^']*')?(GDS[^']*')?(FTX[^']*'){0,9}(MEA[^']*'){1,9}(DIM[^']*'){0,9}(TMP[^']*')?(RNG[^']*')?(LOC[^']*'){0,9}(RFF[^']*')((EQD[^']*')(EQA[^']*'){0,9}(NAD[^']*')?){0,3}
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"LOC"*10000+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(LOC[^\']*\')(GID[^\']*\')?(GDS[^\']*\')?(FTX[^\']*\'){0,9}(MEA[^\']*\'){1,9}(DIM[^\']*\'){0,9}(TMP[^\']*\')?(RNG[^\']*\')?(LOC[^\']*\'){0,9}(RFF[^\']*\')((EQD[^\']*\')(EQA[^\']*\'){0,9}(NAD[^\']*\')?){0,3}";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("LOC");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
//            boolean isMatch = Pattern.matches(regex, attackString);
            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 10000 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
