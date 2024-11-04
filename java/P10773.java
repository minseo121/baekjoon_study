import java.util.*;

public class P10773 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i=0; i<n; i++){
           int a = sc.nextInt();
           if(a == 0){
            stack.pop();
           }else{
            stack.push(a);
           }
        }
        if(stack.isEmpty()){
            System.out.println('0');
            return;
        }
        while(!stack.isEmpty()){
            int num = stack.pop();
            sum += num;
        }
        System.out.println(sum);
    }
}
