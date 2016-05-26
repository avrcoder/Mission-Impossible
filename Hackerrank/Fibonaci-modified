/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;
/* Here we had to use Big Integer because the range exceeds the normal 64 bit value for some cases.
/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	static BigInteger Fibo(int n, BigInteger a, BigInteger b){
		BigInteger f[] = new BigInteger[n];
		f[0] = a;
		f[1] = b;
		for(int i=2;i<n;i++) f[i] = f[i-1].multiply(f[i-1]).add(f[i-2]);
		return f[n-1];
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		BigInteger a = sc.nextBigInteger();
		BigInteger b = sc.nextBigInteger();
		int n = sc.nextInt();
		System.out.println((Fibo(n,a,b)));
	}
}
