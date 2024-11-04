import java.util.Scanner;

public class P2750 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        insertionSort(arr);
        int prev = Integer.MIN_VALUE; // 이전에 출력한 값 저장
        for (int i = 0; i < n; i++) {
            if (arr[i] != prev) { // 현재 값이 이전에 출력한 값과 다를 때만 출력
                System.out.print(arr[i] + " ");
                prev = arr[i];
            }
        }
    }
    
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int tmp = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > tmp) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = tmp;
        }
    }
}
