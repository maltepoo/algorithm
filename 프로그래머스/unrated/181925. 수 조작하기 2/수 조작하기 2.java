class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        
        for (int i = 1; i<numLog.length; i++) {
            int prev = numLog[i-1];
            int cur = numLog[i];
            
            if (cur-prev == 1) {
                answer += "w";
            } else if (cur-prev == -1) {
                answer += "s";
            } else if (cur-prev == 10) {
                answer += "d";
            } else if (cur-prev == -10) {
                answer += "a";
            }
        }
        
        return answer;
    }
}