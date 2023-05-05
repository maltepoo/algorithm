import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> temp = new ArrayList<>();
        
        for (int n: arr) {
            for (int i = 0; i < n; i++) {
                temp.add(n);
            } 
        }
        
        return temp.stream().mapToInt(Integer::intValue).toArray();
    }
}