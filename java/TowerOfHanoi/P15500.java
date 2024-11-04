package TowerOfHanoi;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class P15500 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int targetNum = n;
        int count = 0;
        StringBuilder sb = new StringBuilder();
        Stack<Integer> first = new Stack<>();
        Stack<Integer> second = new Stack<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            first.push(Integer.parseInt(st.nextToken()));
        }
        while (targetNum>0){
            if(first.search(targetNum)>=0){
                while (first.size()>0) {
                    int now = first.pop();
                    if(now == targetNum){
                        sb.append("1 3\n");
                        count ++;
                        targetNum--;
                        break;
                    }else{
                        sb.append("1 2\n");
                        count++;
                        second.add(now);
                    }
                }
            }else if(second.search(targetNum)>=0){
                while (second.size()>0) {
                    int now = second.pop();
                    if(now == targetNum){
                        sb.append("2 3\n");
                        count ++;
                        targetNum--;
                        break;
                    }else{
                        sb.append("2 1\n");
                        count++;
                        first.add(now);
                    }
                }
            }
        }
        System.out.println(count);
        System.out.println(sb.toString());
    }
    
}
