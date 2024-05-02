import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class P11931 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = sc.nextInt();
        int[] data = new int[n];
        for (int i = 0; i < n; i++) {
            data[i] = sc.nextInt();
        }

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (data[i] > max) max = data[i];
            if (data[i] < min) min = data[i];
        }

        int[] cnt = new int[max - min + 1];

        for (int i = 0; i < n; i++) {
            cnt[data[i] - min]++;
        }

        int[] sorted = new int[n];
        int idx = 0;
        for (int i = cnt.length - 1; i >= 0; i--) {
            while (cnt[i] > 0) {
                sorted[idx++] = i + min;
                cnt[i]--;
            }
        }

        for (int i = 0; i < sorted.length; i++) {
            bw.write(sorted[i] + "\n");
        }
        bw.flush();
        bw.close();
    }
}