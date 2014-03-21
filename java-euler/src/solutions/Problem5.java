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
	
	public static void main(String[] args) {
		int i, div = 1;
		for (i = 2; i < 21; i++)
			div = lcm(i, div);
		System.out.println(div);
	}
}