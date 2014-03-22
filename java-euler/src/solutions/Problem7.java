package solutions;

/*
 * Problem:
 * 	By listing the first six prime numbers: 
 * 	2, 3, 5, 7, 11, and 13, we can see that the 
 * 	6th prime is 13.
 * 
 * 	What is the 10,001st prime number?
 * 
 * Answer: 104743
 */
public class Problem7 {
	
	public static void main(String[] args) {
		int count = 1, i = 3;
		while (true) {
			if (Helpers.is_prime(i))
				count += 1;
			if (count == 10001) {
				System.out.println(i);
				break;
			}
			i += 2;
		}
	}
}