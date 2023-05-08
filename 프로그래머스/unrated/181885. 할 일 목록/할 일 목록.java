import java.util.*;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        String[] answer = {};
        List<String> notFinished = new ArrayList<String>();
        
        for (int i = 0; i<finished.length; i++) {
            if (finished[i] == false) {
                notFinished.add(todo_list[i]);
            }
        }
        
        answer = notFinished.toArray(new String[notFinished.size()]);
        return answer;
    }
}