package solutions;

/*
 * Problem:
 * 	A palindromic number reads the same both ways. The 
 * 	largest palindrome made from the product of two 2-digit 
 * 	numbers is 9009 = 91 99.
 * 
 * 	Find the largest palindrome made from the product of two 
 * 	3-digit numbers.
 * 
 * Answer: 906609
 */
public class Problem4 {

	public static void main(String[] args) {
		final int min = 100, max = 999;
		int i, j, max_palindrome = 0, result = 0;
		
		for (i = max; i > min-1; i--) {
			for (j = i-1; j > min-1; j--) {
				result = i*j;
				if (Helpers.is_palindrome(String.valueOf(result)) 
						&& result > max_palindrome)
					max_palindrome = result;
			}
		}
		
		System.out.println(max_palindrome);
	}

}