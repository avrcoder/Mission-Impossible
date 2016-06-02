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
		int t = sc.nextInt();
		while(t>0){
			int g = sc.nextInt();
			while(g>0){
				int i = sc.nextInt();
				long n = sc.nextLong();
				int q = sc.nextInt();
				if(n%2 == 0) System.out.println(n/2);
				else{
					if(i==q) System.out.println(n/2);
					else System.out.println(n-(n/2));
				}
				g--;
			}
			t--;
		}
	}
}
