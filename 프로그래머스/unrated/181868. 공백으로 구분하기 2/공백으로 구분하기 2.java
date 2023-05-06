class Solution {
    public String[] solution(String my_string) {
        String[] answer = {};
        
        answer = my_string.replaceAll("\\s+", " ").trim().split(" ");
        
        return answer;
    }
}