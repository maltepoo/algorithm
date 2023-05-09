import java.util.*;

class Solution {
    public String[] solution(String[] names) {
        String[] answer = {};
        List<String> temp = new ArrayList<String>();
        
        for (int i = 0; i<names.length; i+=5) {
            temp.add(names[i]);
        }
        
        answer = temp.toArray(String[]::new);
        return answer;
    }
}