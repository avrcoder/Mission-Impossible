/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		long a = sc.nextLong();
		int n = sc.nextInt();
		int k = sc.nextInt();
		n++;
		while(k-->0){
			System.out.print(a%n+" ");
			a = a/n;
		}
		System.out.println();
	}
}
