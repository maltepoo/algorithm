import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList<Integer>();
        
        int i = 0;
        
        while (i < arr.length) {
            int stkSize = stk.size();
            if (stkSize == 0) {
                stk.add(arr[i]);
                i++;
            } else {
                if (stk.get(stkSize-1) < arr[i]) {
                    stk.add(arr[i]);
                    i++;
                } else {
                    stk.remove(stkSize-1);
                }
            }
        }
        
        int[] answer = stk.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        return answer;
    }
}