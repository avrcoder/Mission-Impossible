import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    	int n = sc.nextInt();
    	long a[] = new long[n];
    	for(int i=0;i<n;i++) a[i] = sc.nextLong();
    	int b[] = new int[n];
    	for(int i=0;i<n;i++) b[i] = 1;
        int c[] = new int[n];
    	for(int i=0;i<n;i++) c[i] = 1;        
    	for(int i=0;i<n-1;i++){
    		if(a[i+1]>a[i]) b[i+1] = b[i]+1;
    		else b[i+1] = 1;
    	} 
    	for(int i=n-1;i>0;i--){
    		if(a[i-1]>a[i]) c[i-1] = c[i]+1;
            else c[i-1] = 1;
    	}
        for(int i=0;i<n;i++) c[i] = Math.max(b[i],c[i]);
    	long sum = 0;
    	for(int i=0;i<n;i++) sum = sum + c[i];
    	System.out.println(sum);
    }
}
