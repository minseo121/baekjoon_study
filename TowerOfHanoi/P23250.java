package TowerOfHanoi;
import java.util.Scanner;

public class P23250 {
    private static StringBuilder sb = new StringBuilder();
    private static int count = 0;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        if (n <= 60) {
            hanoi(n, 1, 2, 3, k - 1);
            System.out.print(sb);
        }
    }

    public static void hanoi(int n, int start, int middle, int finish, int k) {
        if (n == 1) {
            count++;
            if (count == k + 1) {
                sb.append(start + " " + finish + System.lineSeparator());
            }
            return;
        }
        hanoi(n - 1, start, finish, middle, k);
        count++;
        if (count == k + 1) {
            sb.append(start + " " + finish + System.lineSeparator());
        }
        hanoi(n - 1, middle, start, finish, k);
    }
}
