package _1978;

import java.util.*;
public class _1978 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int nums[] = new int[n];
		
		
		for (int i = 0; i < n; i++) {
			nums[i] = sc.nextInt();
		}
		
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			if (check(nums[i])) {
				cnt++;
			}
			else {
				continue;
			}
		}
		
		System.out.println(cnt);
		
		
	}
	
	public static boolean check(int n) {
		if (n == 1) {
			return false;
		}
		
		if (n == 2) {
			return true;
		}
		for (int i = 2; i < Math.sqrt((n)) + 1; i++) {
			if ( n % i == 0) {
				return false;
			}
		}
		return true;
	}

}
