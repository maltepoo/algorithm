import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n+1];
        int[] lis = new int[n+1];

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            lis[i] = 1;
        }

        int maxN = 1;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    lis[i] = Math.max(lis[i], lis[j]+1);
                }
            }
            maxN = Math.max(maxN, lis[i]);
        }
        bw.write(Integer.toString(maxN));
        br.close();
        bw.flush();
        bw.close();
    }
}