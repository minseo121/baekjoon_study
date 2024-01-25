import java.util.*;

public class P1065{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n<=99){
            System.out.println(n);
        }else if(n>=100){
            int count = 0;
            for(int i=1; i<=n; i++){
                if(i<100){
                    count +=1;
                }else{
                    int a = i/100;
                    int b = (i%100)/10;
                    int c = i%10;
                    if((c - b) == (b - a)){
                        count += 1;
                    }
                }
            }
            System.out.println(count);
        }
    }
}