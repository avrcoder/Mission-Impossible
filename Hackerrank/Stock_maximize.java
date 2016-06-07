package JAVA;
import java.util.*;
import java.io.*;
import java.lang.*;

public class stock_max {
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int t = sc.nextInt();
    	while(t-->0){
    		int n = sc.nextInt();
    		int a[] = new int[n];
    		for(int i=0;i<n;i++) a[i] = sc.nextInt();
    		int max = a[n-1];
    		int profit = 0;
    		for(int i=n-1;i>=0;i--){
    			if(a[i]>max) max = a[i];
    			profit = profit + (max-a[i]);
    		}
    		System.out.println(profit);
    	}
    }
}
