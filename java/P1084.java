import java.util.*;

public class P1084 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();

        int n = sc.nextInt();
        int[] A= new int[n];
        for(int i=0; i<n; i++){
            int a=sc.nextInt();
            A[i] = a;
        }
        Stack<Integer> stack = new Stack<>();
        StringBuffer bf = new StringBuffer();
        boolean result = true;
        int num=1;
        for(int i=0; i < n; i++){
            int b=A[i];
            if(b >= num){
                while (b>=num) {
                    stack.push(num);
                    bf.append("+\n");
                    num++;
                }
                stack.pop();
                bf.append("-\n");
            }
            else{
                int c = stack.pop();
                if(c>b){
                    System.out.println("no");
                    result = false;
                    break;
                }
                else{
                    bf.append("-\n");
                }
            }
        }
        if(result) System.out.println(bf.toString());
    }
}
