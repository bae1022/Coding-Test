import java.io.*;
import java.util.*;

class P{
	private int l;
	private int h;
	
	public P(int l, int h) {
		this.l = l;
		this.h = h;
	}
	
	public int getL() {
		return this.l;
	}
	public int getH() {
		return this.h;
	}
}

public class _2304 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		P[] p = new P[n];
		
		int min_l = 10000;
		int max_l = -1;
		int max_h_index = -1;
		int max_h_val = -1;
		
		for (int i = 0; i < n; i++) {
			int l = sc.nextInt();
			int h = sc.nextInt();
			
			p[i] = new P(l, h);
			
			if (l < min_l) {
				min_l = l;
			}
			
			if (l > max_l) {
				max_l = l;
			}
			
			if (h > max_h_val) {
				max_h_val = h;
				max_h_index = l;
			}
			
		}
		
		int[] p_h_list = new int[max_l + 1];
		
		for (int i = 0; i < n; i++) {
			int a = p[i].getL();
			int b = p[i].getH();
			
			p_h_list[a] = b;
		}
		
		int temp = 0;
		int total = 0;
		
		for (int i = 0; i < max_h_index + 1; i++) {
			if (p_h_list[i] > temp) {
				temp = p_h_list[i];	
				
			}
			
			
			total += temp;
		}
		
		temp = 0;
		for (int i = max_l; i > max_h_index; i--) {
			if (p_h_list[i] > temp) {
				temp = p_h_list[i];
			}
			
			total += temp;
		}
		
		System.out.println(total);
	}

}
