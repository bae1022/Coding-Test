package _2581;

import java.util.*;
public class _2581 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int sum = 0;
		int min_prime = 0;
		int state = 0;
		
		for (int i = n; i <= m; i++) {
			if (state == 0 && check(i)) {
				min_prime = i;
				state = 1;
			}
			
			if (check(i)) {
				sum += i;
			}
		}
		
		if (state == 1) {
			System.out.println(sum);
			System.out.println(min_prime);
		}
		else {
			System.out.println(-1);
		}
		
	}
	
	public static boolean check(int n) {
		if (n == 1) {
			return false;
		}
		
		if (n == 2) {
			return true;
		}
		
		for (int i = 2; i < Math.sqrt(n) + 1; i++) {
			if (n % i == 0) {
				return false;
			}
		}
		
		return true;
	}

}
