import java.util.*;

public class P11650_2 {
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       int n = scanner.nextInt();
       int[][] points = new int[n][2];

       for (int i = 0; i < n; i++) {
           points[i][0] = scanner.nextInt();
           points[i][1] = scanner.nextInt();
       }

       heapSort(points);

       for (int i = 0; i < n; i++) {
           System.out.println(points[i][0] + " " + points[i][1]);
       }
   }

   // 힙 정렬
   public static void heapSort(int[][] arr) {
       int n = arr.length;

       // 최대 힙 구성
       for (int i = n / 2 - 1; i >= 0; i--) {
           heapify(arr, n, i);
       }

       // 힙에서 최대값 추출 후 힙 재구성
       for (int i = n - 1; i > 0; i--) {
           // 최대값(루트)과 마지막 노드 교환
           swap(arr, 0, i);

           // 루트 노드에 대해 heapify
           heapify(arr, i, 0);
       }
   }

   private static void heapify(int[][] arr, int n, int i) {
       int largest = i; // 루트를 largest로 초기화
       int left = 2 * i + 1; // 왼쪽 자식
       int right = 2 * i + 2; // 오른쪽 자식

       // 왼쪽 자식이 largest보다 크면 largest 갱신
       if (left < n && compare(arr[left], arr[largest]) > 0)
           largest = left;

       // 오른쪽 자식이 largest보다 크면 largest 갱신
       if (right < n && compare(arr[right], arr[largest]) > 0)
           largest = right;

       // largest가 변경된 경우 heapify 수행
       if (largest != i) {
           swap(arr, i, largest);
           heapify(arr, n, largest);
       }
   }

   private static void swap(int[][] arr, int i, int j) {
       int[] temp = arr[i];
       arr[i] = arr[j];
       arr[j] = temp;
   }

   private static int compare(int[] a, int[] b) {
       if (a[0] < b[0]) return -1;
       else if (a[0] > b[0]) return 1;
       else {
           if (a[1] < b[1]) return -1;
           else if (a[1] > b[1]) return 1;
           else return 0;
       }
   }
}
