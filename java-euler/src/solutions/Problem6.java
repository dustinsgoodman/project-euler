package solutions;

/*
 * Problem:
 * 	The sum of the squares of the first ten natural numbers is,
 * 
 * 		1^2 + 2^2 + ... + 10^2 = 385
 * 
 * 	The square of the sum of the first ten natural numbers is,
 * 
 * 		(1 + 2 + ... + 10)^22 = 55^22 = 3025
 * 
 * 	Hence the difference between the sum of the squares of the 
 * 	first ten natural numbers and the square of the sum is 
 * 	3025 - 385 = 2640.
 * 	
 * 	Find the difference between the sum of the squares of the 
 * 	first one hundred natural numbers and the square of the sum.
 * 
 * Answer: 25164150
'''
 */
public class Problem6 {

	
	
	public static void main(String[] args) {
		long n = 100,
			 sos = Helpers.sumOfSquares(n),
			 son = Helpers.sumOfNums(n);
		System.out.println(son*son - sos);
	}

}
