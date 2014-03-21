package solutions;

import java.util.ArrayList;

/*
 * Problem:
 * 	The prime factors of 13195 are 5, 7, 13 and 29.
 * 	What is the largest prime factor of the number 600851475143?
 * 
 * Answer: 6857
 */
public class Problem3 {

	public static void main(String[] args) {
		long max = 0;
		ArrayList<Long> factors = Helpers.factor(600851475143L);
		
		for (long factor: factors) {
			if (Helpers.isPrime(factor) && factor > max) {
				max = factor;
			}
		}
		
		System.out.println(max);
	}

}