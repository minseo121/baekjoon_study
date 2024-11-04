import java.util.*;

public class P11659 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
        int m = sc.nextInt();

        int[] arr = new int[n + 1];
        arr[0] = 0;
        for(int a=0; a < n; a++){
            arr[a+1] = arr[a] + sc.nextInt();
        }
        for (int a=0; a < m; a++){
            int i = sc.nextInt();
            int j = sc.nextInt();
            System.out.println(arr[j]-arr[i-1]);
        }
	}
}