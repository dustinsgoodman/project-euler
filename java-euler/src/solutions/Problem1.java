package solutions;

/*
 * Problem:
 *	If we list all the natural numbers below 10 that are mutliples of 3 or 5,
 *	we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
 *	all the multiples of 3 or 5 below 1000.
 *
 * Answer: 233168
 */
public class Problem1 {

	/*
	 * Solution using equation S = d * int(x/d) * (1 + int(x/d)) / 2 
	 * where d is the number we're finding multiples of and x is the 
	 * limiting factor to the numbers we are finding subtracted by 1.
	 * 
	 * @param n		value to find mutliples of
	 * @param limit	limiting factor to the numbers we are finding
	 * @return 		the sum of multiples of n to limit
	 */
	public static int sumNaturalN(int n, int limit) {
		limit -= 1;
		return n * (limit / n) * ((1 + (limit / n )) / 2);
	}

	/*
	 * Add multiples of 3 and 5 and substract multiples of 15 because 
	 * both multiples of 3 and multiples of 5 will find all the sets 
	 * of 15. Hence, there are 2 sets of 15 so we need to remove one 
	 * from the answer.
	 */
	public static void main(String[] args) {
		int answer = 0;
		
		answer += sumNaturalN(3, 1000);
		answer += sumNaturalN(5, 1000);
		answer -= sumNaturalN(15, 1000);
		
		System.out.println(answer);
	}

}