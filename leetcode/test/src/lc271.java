import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class lc271 {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuffer sb = new StringBuffer();
        for (String word : strs) {
            sb.append(word.length());
            sb.append('#');
            sb.append(word);
        }
        System.out.println(sb.toString());
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> ret = new ArrayList<String>();
        for (int i = 0; i < s.length(); i++) {
            int left = i;
            while (i+1 < s.length() && Character.isDigit(s.charAt(i+1))) {
                i++;
            }
            int size = Integer.parseInt(s.substring(left, i+1));
            i++;
            String temp = s.substring(i+1, i+1+size);
            System.out.println(size + " "  + temp);
            ret.add(temp);
            i += size;
        }
        return ret;
    }

    public static void main(String[] args) {
        lc271 t = new lc271();
        List<String> test = new ArrayList<>(Arrays.asList("63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "));
        String d = t.encode(test);
        System.out.println(d);
        System.out.println(t.decode(d));
    }
}