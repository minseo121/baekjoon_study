package TowerOfHanoi;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

public class P1914 {
  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(bf.readLine());
    BigInteger count = new BigInteger("2");
    System.out.println(count.pow(n).subtract(new BigInteger("1")));
    if(n<=20){
    hanoi(n, 1, 2, 3);
    }
  }    
  public static void hanoi(int n, int start, int middle, int finish){
    if(n==1){
      System.out.println(start + " " + finish);
      return;
    }
    hanoi(n-1, start, finish, middle);
    System.out.println(start + " " + finish);
    hanoi(n-1, middle, start, finish);
  }
}
