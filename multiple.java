import java.util.*;
public class multiple {
    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
        int N = in.nextInt();
        for( int m=0; m<N; m++){
            int A = in.nextInt();
            int B = in.nextInt();
            int max = Integer.MIN_VALUE;
            for (int i=1; i<=A && i<=B ; i++){
                if(A%i==0 && B%i==0){
                    max = i;
                }
            }
            int sum1 = A/max;
            int sum2 = B/max;
            System.out.print(sum1 * sum2 * max);
            System.out.print("\n");
        }
    }
}
