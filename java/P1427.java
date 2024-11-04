import java.util.*;

public class P1427 {
    static void swap(ArrayList<Integer> arrNum, int idx1, int idx2) {
        int t = arrNum.get(idx1);
        arrNum.set(idx1, arrNum.get(idx2));
        arrNum.set(idx2, t);
    }

    static void quickSort(ArrayList<Integer> arrNum, int left, int right) {
        if (left >= right) return;

        int pl = left;
        int pr = right;
        int x = arrNum.get((pl + pr) / 2);

        do {
            while (arrNum.get(pl) > x) pl++;
            while (arrNum.get(pr) < x) pr--;
            if (pl <= pr) {
                swap(arrNum, pl, pr);
                pl++;
                pr--;
            }
        } while (pl <= pr);

        quickSort(arrNum, left, pr);
        quickSort(arrNum, pl, right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> arrNum = new ArrayList<>();
        while (n > 0) {
            arrNum.add(n % 10);
            n /= 10;
        }
        quickSort(arrNum, 0, arrNum.size() - 1);
        
        for (int i = 0; i < arrNum.size(); i++) {
            System.out.print(arrNum.get(i));
        }
    }
}
