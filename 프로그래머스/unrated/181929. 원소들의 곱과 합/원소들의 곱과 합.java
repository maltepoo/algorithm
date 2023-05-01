import java.util.Arrays;

class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        int multi = Arrays.stream(num_list).reduce((x, y) -> x*y).getAsInt();
        int sumPow = (int) Math.round(Math.pow(Arrays.stream(num_list).sum(), 2));
        
        if (multi < sumPow) {
            answer = 1;
        }
        
        return answer;
    }
}