package _1292;

import java.util.*;
public class _1292 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		ArrayList<Integer> nums = new ArrayList<>();
		
		int n = 1;
		int cnt = 0;
		for (int i = 0; i < 1000; i++) {
			nums.add(n);
			cnt++;
			
			if (cnt == n) {
				n++;
				
				cnt = 0;
			}
		}
		
		int answer = 0;
		for (int i = a - 1; i <= b - 1; i++) {
			answer += nums.get(i);
		}
		
		System.out.println(answer);
		
		
	}

}
