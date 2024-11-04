import java.util.*;

public class average { //1546번 평균 문제
    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
        int N = in.nextInt();
        double sum =0;
        double max = Integer.MIN_VALUE;
        for (int a=0; a<N; a++){
            int M = in.nextInt();
            if(M > max) {
                max = M;
            }
            sum += M;
        }
        in.close();
        System.out.print(((sum/max)*100)/N);
    }
}
