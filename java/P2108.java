import java.util.*;

public class P2108 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr=new int[n];
        int sum = 0;

        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
            sum += arr[i];
        }
        heapSort(arr);

        int max = arr[n - 1];
        int min = arr[0];

        int[] freq = new int[max - min + 1];
        int maxFreq = 0;
        int mode = 0;
        boolean multipleModes = false;

        for (int num = 0; num < arr.length; num++) {
            freq[num - min]++;
            if (freq[num - min] > maxFreq) {
                maxFreq = freq[num - min];
                mode = num;
                multipleModes = false;
            } else if (freq[num - min] == maxFreq) {
                multipleModes = true;
            }
        }

        if (multipleModes) {
            int modeCount = 0;
            for (int i = 0; i < freq.length; i++) {
                if (freq[i] == maxFreq) {
                    if (modeCount == 1) {
                        mode = i + min;
                        break;
                    }
                    modeCount++;
                }
            }
        }
        System.out.println((int) Math.round((double) sum / n));
        System.out.println(arr[n/2]);
        System.out.println(mode);
        System.out.println(max-min);
    }
    public static void heapSort(int[] arr){
        for (int i=arr.length / 2 - 1; i>=0;i--){
            heapify(arr, arr.length, i);
        }
        for (int i = arr.length- 1; i > 0; i--) {
            swap(arr, 0, i);
            heapify(arr, i, 0);
        }
    }
    public static void heapify(int[] arr, int n, int i){
        int largest=i;
        int left=2*i +1;
        int right=2*i+2;

        if(left < n && arr[left] > arr[largest])
            largest=left;
        if(right < n && arr[right] > arr[largest] )
            largest=right;
        if(largest != i){
            swap(arr, i, largest);
            heapify(arr, n, largest);
        }
    }
    private static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
}
