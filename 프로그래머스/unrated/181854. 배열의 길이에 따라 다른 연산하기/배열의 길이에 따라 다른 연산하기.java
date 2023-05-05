import java.util.*;

class Solution {
    public int[] solution(int[] arr, int n) {
        int arrSize = arr.length;
        int[] answer = Arrays.copyOf(arr, arrSize);
        
        for (int i = 0; i<arrSize; i++) {
            if (arrSize % 2 == 0 && i % 2 == 1) {
                answer[i] = answer[i]+n;
            } else if (arrSize % 2 == 1 && i % 2 == 0) {
                answer[i] = answer[i]+n;
            }
        }
        
        return answer;
    }
}