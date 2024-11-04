import java.util.*;

public class P1181 {
    static void swap(String[] a, int idx1, int idx2) {
        String t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void quickSort(String[] a, int left, int right) {
        int pl = left;
        int pr = right;
        String x = a[(pl + pr) / 2];

        do {
            while (a[pl].compareTo(x) < 0) pl++;
            while (a[pr].compareTo(x) > 0) pr--;
            if (pl <= pr) {
                swap(a, pl++, pr--);
            }
        } while (pl <= pr);

        if (left < pr) quickSort(a, left, pr);
        if (pl < right) quickSort(a, pl, right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String[] words = new String[n];

        // 단어 입력
        for (int i = 0; i < n; i++) {
            words[i] = sc.next();
        }

        // 정렬
        quickSort(words, 0, n - 1);

        // 중복 제거 후 출력
        for (int i = 0; i < n; i++) {
            if (i == 0 || !words[i].equals(words[i - 1])) {
                System.out.println(words[i]);
            }
        }
    }
}
