class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length+1];
        
        // 배열 복사
        for (int i = 0; i < num_list.length; i++) {
            answer[i] = num_list[i];
        }
            
        // 배열 마지막 원소 할당
        int lastIdx = num_list.length - 1;
        if (num_list[lastIdx] > num_list[lastIdx-1]) {
            answer[answer.length-1] = num_list[lastIdx] - num_list[lastIdx-1];
        } else {
            answer[answer.length-1] = num_list[lastIdx]*2;
        }
        
        return answer;
    }
}