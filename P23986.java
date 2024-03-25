import java.util.*;

public class P23986 {
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
                    sum ++; //for문이 돌때마다 sum 값을 증가시킴
                    if(sum == k){//증가시킨 sum값이 k랑 동일하면
                        for(int a=0; a<n; a++){
                        System.out.print(num[a]+" "); //모든 인덱스의 값이 나오도록 하고
                        }
                        return;//끝내기
                    }
                }
            }
        }
        if(sum < k){ //만약 다 돌았는데도 sum값이 k보다 작다면
            System.out.println("-1");//-1을 출력
        }
    }
}
