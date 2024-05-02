import java.util.Scanner;

public class P11651 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(arr[i][j] > max)
                    max = arr[i][j];
                if(arr[i][0] < min)
                    min = arr[i][j];
            }
        }
        int[] cnt;
        if(min>=0){
            cnt = new int[max+1];
        }else{
            cnt = new int[max-min +1];
        }
        for(int i=0; i<n; i++){
            cnt[arr[i][1]-min]++;
        }

        for(int i=0; i<cnt.length; i++){
            while(cnt[i]>0){
                for(int j=0; j<n; j++){
                    if( i+min == arr[j][1]){
                        System.out.println(arr[j][0] +" "+ (i+min));
                    }
                    cnt[i]--;
                }
                
            }
        }
    }
    
}
