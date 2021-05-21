import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexlib_1091 {
    /* 1091
     * (?:(?:w{3}\.)(?:[a-zA-Z0-9/;\?&=:\-_\$\+!\*'\(\|\\~\[\]#%\.])+[\.com|\.edu|\.gov|\.int|\.mil|\.net|\.org|\.biz|\.info|\.name|\.pro|\.aero|\.coop|\.museum|\.cat|\.jobs|\.travel|\.arpa|\.mobi|\.ac|\.ad|\.ae|\.af|\.ag|\.ai|\.al|\.am|\.an|\.ao|\.aq|\.ar|\.as|\.at|\.au|\.aw|\.az|\.ax|\.ba|\.bb|\.bd|\.be|\.bf|\.bg|\.bh|\.bi|\.bj|\.bm|\.bn|\.bo|\.br|\.bs|\.bt|\.bv|\.bw|\.by|\.bz|\.ca|\.cc|\.cd|\.cf|\.cg|\.ch|\.ci|\.ck|\.cl|\.cm|\.cn|\.co|\.cr|\.cs|\.cu|\.cv|\.cx|\.cy|\.cz|\.de|\.dj|\.dk|\.dm|\.do|\.dz|\.ec|\.ee|\.eg|\.eh|\.er|\.es|\.et|\.eu|\.fi|\.fj|\.fk|\.fm|\.fo|\.fr|\.ga|\.gb|\.gd|\.ge|\.gf|\.gg|\.gh|\.gi|\.gl|\.gm|\.gn|\.gp|\.gq|\.gr|\.gs|\.gt|\.gu|\.gw|\.gy|\.hk|\.hm|\.hn|\.hr|\.ht|\.hu|\.id|\.ie|\.il|\.im|\.in|\.io|\.iq|\.ir|\.is|\.it|\.je|\.jm|\.jo|\.jp|\.ke|\.kg|\.kh|\.ki|\.km|\.kn|\.kp|\.kr|\.kw|\.ky|\.kz|\.la|\.lb|\.lc|\.li|\.lk|\.lr|\.ls|\.lt|\.lu|\.lv|\.ly|\.ma|\.mc|\.md|\.mg|\.mh|\.mk|\.ml|\.mm|\.mn|\.mo|\.mp|\.mq|\.mr|\.ms|\.mt|\.mu|\.mv|\.mw|\.mx|\.my|\.mz|\.na|\.nc|\.ne|\.nf|\.ng|\.ni|\.nl|\.no|\.np|\.nr|\.nu|\.nz|\.om|\.pa|\.pe|\.pf|\.pg|\.ph|\.pk|\.pl|\.pm|\.pn|\.pr|\.ps|\.pt|\.pw|\.py|\.qa|\.re|\.ro|\.ru|\.rw|\.sa|\.sb|\.sc|\.sd|\.se|\.sg|\.sh|\..si|\.sj|\.sk|\.sl|\.sm|\.sn|\.so|\.sr|\.st|\.sv|\.sy|\.sz|\.tc|\.td|\.tf|\.tg|\.th|\.tj|\.tk|\.tl|\.tm|\.tn|\.to|\.tp|\.tr|\.tt|\.tv|\.tw|\.tz|\.ua|\.ug|\.uk|\.um|\.us|\.uy|\.uz|\.va|\.vc|\.ve|\.vg|\.vi|\.vn|\.vu|\.wf|\.ws|\.ye|\.yt|\.yu|\.za|\.zm|\.zw](?:[a-zA-Z0-9/;\?&=:\-_\$\+!\*'\(\|\\~\[\]#%\.])*)
     * EXPONENT
     * nums:2
     * EXPONENT AttackString:""+"www."*1024+"@1 _SLQ_2"
     */
    public static void main(String[] args) throws InterruptedException {
        String regex = "(?:(?:w{3}\\.)(?:[a-zA-Z0-9/;\\?&=:\\-_\\$\\+!\\*\'\\(\\|\\\\~\\[\\]#%\\.])+[\\.com|\\.edu|\\.gov|\\.int|\\.mil|\\.net|\\.org|\\.biz|\\.info|\\.name|\\.pro|\\.aero|\\.coop|\\.museum|\\.cat|\\.jobs|\\.travel|\\.arpa|\\.mobi|\\.ac|\\.ad|\\.ae|\\.af|\\.ag|\\.ai|\\.al|\\.am|\\.an|\\.ao|\\.aq|\\.ar|\\.as|\\.at|\\.au|\\.aw|\\.az|\\.ax|\\.ba|\\.bb|\\.bd|\\.be|\\.bf|\\.bg|\\.bh|\\.bi|\\.bj|\\.bm|\\.bn|\\.bo|\\.br|\\.bs|\\.bt|\\.bv|\\.bw|\\.by|\\.bz|\\.ca|\\.cc|\\.cd|\\.cf|\\.cg|\\.ch|\\.ci|\\.ck|\\.cl|\\.cm|\\.cn|\\.co|\\.cr|\\.cs|\\.cu|\\.cv|\\.cx|\\.cy|\\.cz|\\.de|\\.dj|\\.dk|\\.dm|\\.do|\\.dz|\\.ec|\\.ee|\\.eg|\\.eh|\\.er|\\.es|\\.et|\\.eu|\\.fi|\\.fj|\\.fk|\\.fm|\\.fo|\\.fr|\\.ga|\\.gb|\\.gd|\\.ge|\\.gf|\\.gg|\\.gh|\\.gi|\\.gl|\\.gm|\\.gn|\\.gp|\\.gq|\\.gr|\\.gs|\\.gt|\\.gu|\\.gw|\\.gy|\\.hk|\\.hm|\\.hn|\\.hr|\\.ht|\\.hu|\\.id|\\.ie|\\.il|\\.im|\\.in|\\.io|\\.iq|\\.ir|\\.is|\\.it|\\.je|\\.jm|\\.jo|\\.jp|\\.ke|\\.kg|\\.kh|\\.ki|\\.km|\\.kn|\\.kp|\\.kr|\\.kw|\\.ky|\\.kz|\\.la|\\.lb|\\.lc|\\.li|\\.lk|\\.lr|\\.ls|\\.lt|\\.lu|\\.lv|\\.ly|\\.ma|\\.mc|\\.md|\\.mg|\\.mh|\\.mk|\\.ml|\\.mm|\\.mn|\\.mo|\\.mp|\\.mq|\\.mr|\\.ms|\\.mt|\\.mu|\\.mv|\\.mw|\\.mx|\\.my|\\.mz|\\.na|\\.nc|\\.ne|\\.nf|\\.ng|\\.ni|\\.nl|\\.no|\\.np|\\.nr|\\.nu|\\.nz|\\.om|\\.pa|\\.pe|\\.pf|\\.pg|\\.ph|\\.pk|\\.pl|\\.pm|\\.pn|\\.pr|\\.ps|\\.pt|\\.pw|\\.py|\\.qa|\\.re|\\.ro|\\.ru|\\.rw|\\.sa|\\.sb|\\.sc|\\.sd|\\.se|\\.sg|\\.sh|\\..si|\\.sj|\\.sk|\\.sl|\\.sm|\\.sn|\\.so|\\.sr|\\.st|\\.sv|\\.sy|\\.sz|\\.tc|\\.td|\\.tf|\\.tg|\\.th|\\.tj|\\.tk|\\.tl|\\.tm|\\.tn|\\.to|\\.tp|\\.tr|\\.tt|\\.tv|\\.tw|\\.tz|\\.ua|\\.ug|\\.uk|\\.um|\\.us|\\.uy|\\.uz|\\.va|\\.vc|\\.ve|\\.vg|\\.vi|\\.vn|\\.vu|\\.wf|\\.ws|\\.ye|\\.yt|\\.yu|\\.za|\\.zm|\\.zw](?:[a-zA-Z0-9/;\\?&=:\\-_\\$\\+!\\*\'\\(\\|\\\\~\\[\\]#%\\.])*)";
        for (int i = 0; i < 1000; i++) {
            StringBuilder attackString = new StringBuilder();
            // 前缀
            attackString.append("");
            // 歧义点
            for (int j = 0; j < i * 10000; j++) {
                attackString.append("www.");
            }
            // 后缀
            attackString.append("@1 _SLQ_2");
//            System.out.println(attackString);
            long time1 = System.nanoTime();
            boolean isMatch = Pattern.matches(regex, attackString);
//            boolean isMatch = Pattern.compile(regex).matcher(attackString).find();
            long time2 = System.nanoTime();
            System.out.println(i * 1 + " " + isMatch + " " + (time2 - time1)/1e9);
        }
    }
}
