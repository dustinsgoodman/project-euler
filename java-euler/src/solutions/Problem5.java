package solutions;

/*
 * Problem:
 * 	2520 is the smallest number that can be divided 
 * 	by each of the numbers from 1 to 10 without any 
 * 	remainder.
 * 
 * 	What is the smallest positive number that is 
 * 	evenly divisible by all of the numbers from 1 
 * 	to 20?
 * 
 * Answer: 232792560
 */
public class Problem5 {
	
	
	
	public static void main(String[] args) {
		int i, div = 1;
		for (i = 2; i < 21; i++)
			div = Helpers.lcm(i, div);
		System.out.println(div);
	}
}