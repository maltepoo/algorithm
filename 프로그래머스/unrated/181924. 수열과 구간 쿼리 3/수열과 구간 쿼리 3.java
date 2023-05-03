class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        
        for (int[] q: queries) {
            int prev = arr[q[0]];
            int next = arr[q[1]];
            
            arr[q[0]] = next;
            arr[q[1]] = prev;
        }
        return arr;
    }
}