import java.util.*;

public class P23968 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int sum = 0;
        int[] num = new int[n];
        for(int i=0; i<n; i++){
            num[i] = sc.nextInt();
        }
        for(int i=0;i<num.length; i++){
            for(int j=0; j<num.length-1; j++){
                if(num[j] > num[j+1]){
                    int temp = num[j];
                    num[j] = num[j + 1];
                    num[j + 1] = temp;
                    sum ++;
                    if(sum == k){
                        System.out.println(num[j]);
                        System.out.println(num[j+1]);
                        return; 
                    }
                }
            }
        }
        if(sum < k){
            System.out.println("-1");
        }
    }
}
