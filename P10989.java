import java.util.*;

public class P10989 {
    static void swap(int[] a, int idx1, int idx2){
        int t=a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }
    static int sort3elem(int[] x, int a, int b, int c){
        if(x[b]<x[a]) swap(x,b,a);
        if(x[c]<x[b]) swap(x,c,b);
        if(x[b]<x[a]) swap(x,b,a);
        return b;
    }
    
    static void quickSort(int[] a, int left, int right){
        int pl = left;        //왼쪽 커서
        int pr = right;      //오른쪽 커서
        int m = sort3elem(a, pl, (pl+pr)/2, pr);    //처음, 가운데, 끝 요소를 정렬
        int x = a[m];        //피벗
        
        swap(a,m,pr-1);      //가운데 요소와 끝에서 두번째 요소 교환
        pl++;                //왼쪽 커서를 오른쪽으로 1 진행
        pr-=2;               //오른쪽 코서를 왼쪽으로 2 만큼 진행
        
        // 피벗 x를 기준으로 배열 a를 나눔
        do{
            while (a[pl] < x) pl++;
            while (a[pr] > x) pr--;
            if(pl <= pr)
                swap(a,pl++,pr--);
        }while(pl<=pr);
        
        //요소 수가 두개 이상일 때 재귀함수 호출
        if(left<pr) quickSort(a, left, pr);
        if(pl<right) quickSort(a,pl,right);
    }
    
public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int[] x=new int[n];
    for(int i=0; i<n; i++){
        x[i] = sc.nextInt();
    }
    quickSort(x, 0, n-1);
    for(int i=0; i<n; i++){
        System.out.println(x[i]+" ");
    }
}
} 
