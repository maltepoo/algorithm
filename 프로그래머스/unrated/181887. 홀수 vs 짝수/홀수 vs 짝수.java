class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        for (int i = 0; i<num_list.length; i+=2) {
            answer += num_list[i];
        }
        
        int odd = 0;
        for (int i = 1; i<num_list.length; i+=2) {
            odd += num_list[i];
        }
        
        answer = Math.max(answer, odd);
        return answer;
    }
}