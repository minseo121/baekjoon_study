import java.util.*;

public class P253052{
    static void swap(int[] a, int idx1, int idx2){
	int t = a[idx1];
	a[idx1] = a[idx2];
	a[idx2] = t;
}

static void quickSort(int[] a, int left, int right){
	int pl = left;        
	int pr = right;      
	int x = a[(pl+pr)/2];   
	
	do{
		while (a[pl] < x) pl++;
		while (a[pr] > x) pr--;
		if(pl <= pr)
			swap(a,pl++,pr--);
	}while(pl<=pr);
	
	if(left < pr) quickSort(a, left, pr);
	if(pl < right) quickSort(a, pl, right);
}

public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	
	int n = sc.nextInt();
	int[] x = new int[n];
    int k = sc.nextInt();
	
	for (int i = 0; i< n; i++){
		x[i] = sc.nextInt();
	}
	
	quickSort(x, 0, n-1);
    System.out.println(x[n-k]);
}	
}