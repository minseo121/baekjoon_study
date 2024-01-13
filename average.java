import java.util.*;

public class average {
    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
        double N = in.nextDouble();
        double sum =0;
        double max = Integer.MIN_VALUE;
        for (int a=0; a<N; a++){
            double M= in.nextDouble();
            if(M > max) {
                max = M;
            }
            sum += M;
        }
        System.out.print(sum);
    }
}
