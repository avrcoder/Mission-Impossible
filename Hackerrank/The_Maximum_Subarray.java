// Here we have used the approach of Kenede's algorithms for solving the max subarray sum instead if Dynamic programming because it solves it in linear time
//For the non contiguous sum we have sorted the array and then calculated the sum in the reverse order





/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	static void Max_sum_array(int[] a,int n){
		int curr_sum = a[0], max_sum = a[0];
		for(int i=1;i<n;i++){
			curr_sum = Math.max(a[i],curr_sum+a[i]);
			max_sum = Math.max(max_sum,curr_sum);
		}
		Arrays.sort(a);
		int max_sum2 = a[n-1];
		for(int i=n-2;i>=0;i--){
			if(max_sum2 + a[i] < max_sum2) break;
			else max_sum2 = max_sum2 + a[i];
		}
		System.out.println(max_sum + " " + max_sum2);
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t>0){
		int n = sc.nextInt();
		int a[] = new int[n];
		for(int i=0;i<n;i++) a[i] = sc.nextInt();
		Max_sum_array(a,n);
            t--;
        }
	}
}
