class Solution {
    public int solution(int n, String control) {        
        for (int i = 0; i < control.length(); i++) {
            char s = control.charAt(i);
            if (s == 'w') {
                n++;
            } else if (s == 's') {
                n--;
            } else if (s == 'd') {
                n += 10;
            } else {
                n -= 10;
            }
        }
        return n;
    }
}