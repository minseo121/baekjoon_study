import java.util.*;

public class P11389 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        int [] P = new int[n];
        for (int i=0; i<n; i++){
            P[i] = sc.nextInt();;
        }
        for (int i=0; i<n-1; i++){
            for(int j=i+1; j<n; j++){
                if(P[i]>P[j]){
                    int a = P[i];
                    P[i] = P[j];
                    P[j] = a;
                }
            }
        }
        for(int i=0; i<n; i++){
            int a = P[i]*(n-i);
            sum += a;
        }
        System.out.println(sum);
    }
}
