package solutions;

/*
 * Problem:
 * 	A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
 * 
 * 		a**2 + b**2 = c**2
 * 
 * 	For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
 * 
 * 	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * 	Find the product abc.
 * 
 * Answer: 31875000
 */
public class Problem9 {

	public static void main(String[] args) {
		int a, b, sum_abc = 1000;
		double c;
		
		for (a = 1; a < sum_abc; a++) {
			for (b = a+1; b < sum_abc; b++) {
				c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
				if (c == Math.floor(c) && a+b+c == 1000) {
					System.out.printf("%d%n",  a*b*(int)c);
				}
			}
		}
	}

}
