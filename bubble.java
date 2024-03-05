import java.util.*;

public class bubble {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int[] num = {1,6,4,2,3,5};
        int a=0;
        for (int i = 0; i < num.length; i++) {
            for (int j = 0; j < num.length-1; j++) {
                if (num[j] > num[j + 1]) {
                    int temp = num[j];
                    num[j] = num[j + 1];
                    num[j + 1] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(num));
    }
}
