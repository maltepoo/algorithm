class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        String myString2 = myString.toLowerCase();
        String pat2 = pat.toLowerCase();
        if (myString2.contains(pat2)) {
            answer = 1;
        }
        
        return answer;
    }
}