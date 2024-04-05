import java.util.*;

public class cntSort {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[] data = new int[n];

        for(int i=0; i<n; i++){
            data[i] = sc.nextInt();
        }

        // 최댓값과 최솟값 찾기
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i=0; i<n; i++){
            if(data[i] > max)
                max = data[i];
            if(data[i] < min)
                min = data[i];
        }
        System.out.println("최댓값 : " + max);
        System.out.println("최솟값 : " + min);

        // 카운트 배열 생성
        int[] cnt;
        if(min >= 0) {
            cnt = new int[max+1];
        } else {
            cnt = new int[max - min + 1];
        }

        // 데이터 카운팅
        for(int i=0; i<n; i++){
            cnt[data[i] - min]++;
        }

        // 정렬된 결과 출력
        for(int i = 0; i < cnt.length; i++){
            while(cnt[i] > 0) {
                System.out.printf((i + min) + " ");
                cnt[i]--;
            }
        }
    }
}
