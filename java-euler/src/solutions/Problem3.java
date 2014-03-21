package solutions;

import java.util.ArrayList;
import java.util.Collections;

/*
 * Problem:
 * 	The prime factors of 13195 are 5, 7, 13 and 29.
 * 	What is the largest prime factor of the number 600851475143?
 * 
 * Answer: 6857
 */
public class Problem3 {

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
	
	public static boolean isPrime(long n) {
		if (n % 2 == 0) return false;
		for (long i = 3; i < Math.sqrt(n) + 1; i += 2) {
			if (n % i == 0) return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		long max = 0;
		ArrayList<Long> factors = factor(600851475143L);
		
		for (long factor: factors) {
			if (isPrime(factor) && factor > max) {
				max = factor;
			}
		}
		
		System.out.println(max);
	}

}