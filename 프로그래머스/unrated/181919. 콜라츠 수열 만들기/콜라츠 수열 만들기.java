import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> seq = new ArrayList<Integer>();
        seq.add(n);
        int m = n;
        
        while (m > 1) {
            if (m % 2 == 0) {
                m = m/2;
            } else {
                m = 3*m+1;
            }
            seq.add(m);
        }
        
        int[] answer = seq.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        return answer;
    }
}