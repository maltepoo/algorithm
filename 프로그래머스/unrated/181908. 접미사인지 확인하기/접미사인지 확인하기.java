class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        
        int n = is_suffix.length();
        int m = my_string.length()-n;
        
        if (m < 0) {
            return answer;
        } else {
            String sliced = my_string.substring(m);
            if (sliced.equals(is_suffix)) {
                answer = 1;
            }
        }
        
        return answer;
    }
}