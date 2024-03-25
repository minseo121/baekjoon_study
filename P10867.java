import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;

public class P10867 {
    static int[] temp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        temp = new int[arr.length];

        mergeSort(arr, 0, arr.length - 1);

        int len = removeDuplicates(arr);

        for (int i = 0; i < len; i++) {
            pw.println(arr[i]);
        }

        pw.flush();
        pw.close();
        br.close();
    }

    public static void mergeSort(int[] arr, int low, int high) {
        if (high - low < 1) {
            return;
        }

        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }

    private static void merge(int[] arr, int low, int mid, int high) {
        int t = 0, l = low, h = mid + 1;

        while (l <= mid && h <= high) {
            if (arr[l] <= arr[h]) {
                temp[t++] = arr[l++];
            } else {
                temp[t++] = arr[h++];
            }
        }

        while (l <= mid) {
            temp[t++] = arr[l++];
        }

        while (h <= high) {
            temp[t++] = arr[h++];
        }

        System.arraycopy(temp, 0, arr, low, t);
    }

    private static int removeDuplicates(int[] arr) {
        if (arr.length == 0 || arr.length == 1) {
            return arr.length;
        }

        int j = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] != arr[i + 1]) {
                arr[j++] = arr[i];
            }
        }
        arr[j++] = arr[arr.length - 1];

        return j;
    }
}
