class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        
        for (int m: numbers) {
            if (answer > n) {
                break;
            }
            answer += m;
        }
        
        return answer;
    }
}