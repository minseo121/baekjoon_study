import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2751 {
    static int[] temp; // 임시 배열을 전역으로 선언하여 반복 생성을 피합니다.

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine()); //데이터 가공
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine()); //데이터 가공
        }

        temp = new int[arr.length]; // 임시 배열 할당

        mergeSort(arr, 0, n);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(arr[i]).append('\n');
        }
        System.out.print(sb.toString());
    }

    public static void mergeSort(int[] arr, int low, int high) {
        if (high - low < 2) {
            return;
        }

        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid, high);
        merge(arr, low, mid, high);
    }

    private static void merge(int[] arr, int low, int mid, int high) {
        int t = 0, l = low, h = mid;

        while (l < mid && h < high) {
            if (arr[l] < arr[h]) {
                temp[t++] = arr[l++];
            } else {
                temp[t++] = arr[h++];
            }
        }

        while (l < mid) {
            temp[t++] = arr[l++];
        }

        while (h < high) {
            temp[t++] = arr[h++];
        }

        // 임시 배열에 병합된 결과를 원본 배열에 복사
        System.arraycopy(temp, 0, arr, low, high - low);
    }
}
