import java.util.*;

public class cntSort {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[] data = new int[n];

        for(int i=0; i<n; i++){
            data[i] = sc.nextInt();
        }

        //최대값 찾기
        int max = data[0]; 
		for(int i=1; i<data.length; i++) { 
			if(max < data[i]) max = data[i]; 
        }
        System.out.println("최댓값 : " + max);

        int[] cnt = new int[max+1];

        for(int i=0; i<n; i++){
            cnt[data[i]]++;
        }
        for(int i = 0; i < max+1; i++){
            while(cnt[i] > 0) {
                System.out.printf(i + " ");
                cnt[i]--;
            }
        }
    }
}