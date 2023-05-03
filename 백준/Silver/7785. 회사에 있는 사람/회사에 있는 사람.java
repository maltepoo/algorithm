import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(bf.readLine());

        HashSet<String> dict = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] nameStatus = bf.readLine().split(" ");
            String name = nameStatus[0];
            String status = nameStatus[1];

            if (status.equals("enter")) {
                dict.add(name);
            } else if (status.equals("leave")){
                dict.remove(name);
            }
        }

        List<String> record = new ArrayList<>(dict);
        Collections.sort(record, Collections.reverseOrder());

        for (String rc: record) {
            bw.write(rc + "\n");
        }

        bf.close();
        bw.flush();
        bw.close();

    }
}