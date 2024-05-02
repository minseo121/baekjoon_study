package TowerOfHanoi;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class P11729 {
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        if (n <= 20 && n >= 1) {
            int totalCount = (int) Math.pow(2, n) - 1;
            bw.write(totalCount + "\n");
            hanoi(n, 1, 2, 3, bw);
        }
        bw.flush();
        bw.close();
    }

    public static void hanoi(int n, int start, int middle, int finish, BufferedWriter bw) throws IOException {
        if (n == 1) {
            bw.write(start + " " + finish + "\n");
            return;
        }
        hanoi(n - 1, start, finish, middle, bw);
        bw.write(start + " " + finish + "\n");
        hanoi(n - 1, middle, start, finish, bw);
    }
}