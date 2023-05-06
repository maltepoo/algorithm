import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = Arrays.copyOf(num_list, num_list.length);
        Arrays.sort(answer);
        answer = Arrays.copyOf(answer, 5);
        
        return answer;
    }
}