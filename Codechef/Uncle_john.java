/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	 static int binary(long a[], int l, int h, long key){
    	int mid = (l+h)/2;
    	if(a[mid] == key) return mid+1;
    	else if(a[mid]<key) return binary(a,mid+1,h,key);
    	else return binary(a,l,mid-1,key);
    }
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t>0){
			int n = sc.nextInt();
			long a[] = new long[n];
			for(int i=0;i<n;i++) a[i] = sc.nextInt();
			int k = sc.nextInt();
			long key = a[k-1];
			Arrays.sort(a);
			System.out.println(binary(a,0,n,key));
			t--;
		}
	}
}
