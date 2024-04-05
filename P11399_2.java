import java.util.*;

public class P11399_2 {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int sum = 0;

        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        heapSort(arr);

        for(int i=0; i<n; i++){
            int a = arr[i]*(n-i);
            sum += a;
        }
        System.out.println(sum);
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