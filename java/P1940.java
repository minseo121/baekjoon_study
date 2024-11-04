import java.util.*;

public class P1940 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int r = 0;
        int [] N = new int[n];
        for(int i=0; i<n; i++){
            int a = sc.nextInt();
            N[i] = a;
        }
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if(N[i]+N[j] == s){
                    r += 1;
                }
            }
        }
        System.out.println(r);
    }
}
