import java.util.Scanner;

public class P2309 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = 9; // 고정된 9명의 키
        int[] data = new int[n];
        int sum = 0;

        for(int i = 0; i < n; i++){
            data[i] = sc.nextInt();
            sum += data[i];
        }

        // 두 명의 키를 선택하여 합이 100이 되는 경우 찾기
        outerLoop:
        for(int i = 0; i < n - 1; i++) {
            for(int j = i + 1; j < n; j++) {
                // 두 명의 키를 제외한 키의 합이 100이 되면 출력
                if(sum - data[i] - data[j] == 100) {
                    int[] toSort = new int[7];
                    int index = 0;
                    for(int k = 0; k < n; k++) {
                        if(k != i && k != j) {
                            toSort[index++] = data[k];
                        }
                    }
                    countingSort(toSort);
                    break outerLoop; // 합이 100이 되는 경우를 찾았으므로 반복문 종료
                }
            }
        }
        
    }
    public static void countingSort(int[] data){
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < data.length; i++){
            if(data[i] > max)
                max = data[i];
            if(data[i] < min)
                min = data[i];
        }

        int[] cnt;
        if(min >= 0) {
            cnt = new int[max + 1];
        } else {
            cnt = new int[max - min + 1];
        }
        for(int i = 0; i < data.length; i++){
            cnt[data[i] - min]++;
        }
        for(int i = 0; i < cnt.length; i++){
            while(cnt[i] > 0) {
                System.out.printf((i + min) + " ");
                cnt[i]--;
            }
        }
    }
}
