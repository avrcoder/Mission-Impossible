package Java;
import java.util.*;
import java.io.*;
import java.lang.*;

public class coinChange {
    static long coinchange(int a[], int n){
    	long t[][] = new long[a.length][n+1];
    	for(int j=0;j<n+1;j++){
    		if(j%a[0]==0) t[0][j] = 1;
    		else t[0][j] = 0;
    	}
    	for(int i=1;i<a.length;i++){
    		for(int j=0;j<=n;j++){
    			if(j<a[i]) t[i][j] = t[i-1][j];
    			else t[i][j] = t[i-1][j] + t[i][j-a[i]];
    		}
    	}
    	return t[a.length-1][n];
    }
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int sum = sc.nextInt();
    	int n = sc.nextInt();
    	int a[] = new int[n];
    	for (int i=0;i<n ;i++ ) {
    		a[i] = sc.nextInt();
    	}
    	System.out.println(coinchange(a,sum));
    }
}

// Here I have used Dynamic programming to solve the problem. First we fill the first row with 1 if it is divisible by the first coin else it will be filled with 0.
//Then we fill the first column with 1 and then the rest are fillid according to the formula above.
