class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for (int q = 0; q<queries.length; q++) {
            int s = queries[q][0];
            int e = queries[q][1];
            int k = queries[q][2];
            
            int minV = 10000001;
            for (int i = s; i<=e; i++) {
                if (arr[i] > k && arr[i] < minV) {
                    minV = arr[i];
                }
            }
            
            if (minV == 10000001) {
                answer[q] = -1;
            } else {
                answer[q] = minV;
            }
        }
        return answer;
    }
}