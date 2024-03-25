import java.util.Arrays;
import java.util.Scanner;

public class P1920 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sum = 0;
        int[] A=new int[n];
        for(int i=0; i<n; i++){
            A[i]=sc.nextInt();
        }
        Arrays.sort(A);
        int m=sc.nextInt();
        for(int i=0; i<m; i++){
            int a=sc.nextInt();
            int low = 0;
            int high = n - 1;
            boolean found = false;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (A[mid] == a) {
                    found = true;
                    break;
                } else if (A[mid] < a) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            if (found) {
                System.out.println('1');
            } else {
                System.out.println('0');
            }
        } 
    }
}
