import java.util.*;

public class P10817 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[3];
        for(int i=0; i<3; i++){
            arr[i] = sc.nextInt();
        }
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i=0; i<3; i++){
            if(arr[i] > max)
                max = arr[i];
            if(arr[i] < min)
                min = arr[i];
        }
        int[] cnt;
        if(min>=0){
            cnt=new int[max+1];
        }else{
            cnt = new int[max-min+1];
        }
        for (int i=0; i<3; i++){
            cnt[arr[i]-min]++;
        }
        int[] sorted = new int[3];
        int idx = 0;
        for(int i=0; i<cnt.length; i++){
            while(cnt[i]>0){
                sorted[idx++] = i + min;
                cnt[i]--;
            }
        }
        System.out.println(sorted[1]);
    }
}
