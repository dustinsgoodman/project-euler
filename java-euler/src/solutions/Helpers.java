package solutions;

import java.util.ArrayList;
import java.util.Collections;

public class Helpers {
	
	public static ArrayList<Long> factor(long n) {
		long i;
		ArrayList<Long> factors = new ArrayList<Long>();
		
		for (i = 1; i < (int) (Math.sqrt(n) + 1); i++) {
			if (n % i == 0) {
				factors.add(i);
				factors.add(n/i);
			}
		}
		
		Collections.sort(factors);
		
		return factors;
	}
	
	public static boolean is_prime(long n) {
		if (n % 2 == 0) return false;
		for (long i = 3; i < Math.sqrt(n) + 1; i += 2) {
			if (n % i == 0) return false;
		}
		return true;
	}
	
	public static boolean is_palindrome(String s) {
		int i, n = s.length();
		for (i = 0; i < (n / 2) + 1; i++)
			if (s.charAt(i) != s.charAt(n-i-1)) return false;
		return true;
	}
	
	public static int gcd(int a, int b) {
		if (b == 0)
			return a;
		else
			return gcd(b, a%b);
	}
	
	public static int lcm(int a, int b) {
		if (a % b == 0)
			return a;
		else if (b % a == 0)
			return b;
		else
			return a*b / gcd(a,b);
	}
	
	public static long sum_of_nums(long n) {
		return n*(n+1)/2;
	}
	
	public static long sum_of_squares(long n) {
		return (n*(n+1)*((2*n)+1))/6;
	}
}
