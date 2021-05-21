import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_5491 {
    /* 5491
     * ((EQD[^']*')(RFF[^']*'){0,9}(EQN[^']*')?(TMD[^']*'){0,9}(DTM[^']*'){0,9}(LOC[^']*'){0,9}(MEA[^']*'){0,9}(DIM[^']*'){0,9}(TMP[^']*'){0,9}(RNG[^']*'){0,9}(SEL[^']*'){0,9}(FTX[^']*'){0,9}(DGS[^']*'){0,9}(EQA[^']*'){0,9}(NAD[^']*')?)((TDT[^']*')(RFF[^']*'){0,9}(LOC[^']*'){0,9}(DTM[^']*'){0,9})?
     * POLYNOMIAL
     * nums:2
     * POLYNOMIAL AttackString:""+"EQD"*10000+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "((EQD[^\']*\')(RFF[^\']*\'){0,9}(EQN[^\']*\')?(TMD[^\']*\'){0,9}(DTM[^\']*\'){0,9}(LOC[^\']*\'){0,9}(MEA[^\']*\'){0,9}(DIM[^\']*\'){0,9}(TMP[^\']*\'){0,9}(RNG[^\']*\'){0,9}(SEL[^\']*\'){0,9}(FTX[^\']*\'){0,9}(DGS[^\']*\'){0,9}(EQA[^\']*\'){0,9}(NAD[^\']*\')?)((TDT[^\']*\')(RFF[^\']*\'){0,9}(LOC[^\']*\'){0,9}(DTM[^\']*\'){0,9})?";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("EQD");
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
