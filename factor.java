import java.util.*;
public class factor { //제출할때에는... Main으로 해야한단다...
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int a = sc.nextInt(); //N의 개수
        int max, min = 0;
        max = Integer.MIN_VALUE; //이거 두개 몰랐음.
        min = Integer.MAX_VALUE;
        //while문을 써서 a를 받고 => a만큼 반복해서 약수 값을 받아야함.
        while(a-- > 0){
            int b=sc.nextInt(); //A 입력 받고
            if(b > max) max = b;
            if(b < min) min = b;
        }
        System.out.print(max*min);
    }
}
