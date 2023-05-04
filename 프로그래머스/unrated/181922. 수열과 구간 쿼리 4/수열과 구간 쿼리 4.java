import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr.clone();
        
        for (int[] q: queries) {
            int s = q[0];
            int e = q[1];
            int k = q[2];
            for (int i = s; i<=e; i++) {
                if (i % k == 0) {
                    answer[i] += 1;
                }
            }
        }
        
        return answer;
    }
}