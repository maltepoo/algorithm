class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String myString2 = "";
        
        for (int i = 0; i<myString.length(); i++) {
            if (myString.charAt(i) == 'A') {
                myString2 += 'B';
            } else {
                myString2 += 'A';
            }
        }
        
        if (myString2.contains(pat)) {
            answer = 1;
        }
        
        return answer;
    }
}