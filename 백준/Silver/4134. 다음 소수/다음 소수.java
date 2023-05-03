import java.io.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(bf.readLine());
        for (int i = 0; i < t; i++) {
            Long n = Long.valueOf(bf.readLine());
            BigInteger prime = new BigInteger(String.valueOf(n));
            
            if (prime.isProbablePrime(10)) {
                // 소수인지 판별하는 함수(10 = certainty)
                bw.write(prime+"\n");
            } else {
                // 소수가 아니라면 다음 소수를 구해서 출력
                bw.write(prime.nextProbablePrime()+"\n");
            }
        }

        bf.close();
        bw.close();
    }
}