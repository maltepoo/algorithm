import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        String[] answer = {};
        List<String> prefix = new ArrayList<>();
        
        for (int i = 0; i<=my_string.length()-1; i++) {
            for (int j = my_string.length(); j>=i; j--) {
                // System.out.println(my_string.substring(i, j));
                prefix.add(my_string.substring(i, j));
                break;
            }
        }
        Collections.sort(prefix);
        answer = prefix.toArray(new String[0]);
        
        return answer;
    }
}