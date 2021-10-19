import java.util.*;
public class _14719 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int h = sc.nextInt();
		int w = sc.nextInt();
		
		int max_h = -1;
		int max_h_index = -1;
		
		int[] heights = new int[w];
		
		for (int i = 0; i < w; i++) {
			heights[i] = sc.nextInt();
			
			if (heights[i] > max_h) {
				max_h = heights[i];
				max_h_index = i;
			}
		}
		
		int temp = 0;
		int sum = 0;
		for (int i = 0; i < max_h_index + 1; i++) {
			if (heights[i] > temp) {
				temp = heights[i];
			}
			sum += temp;
		}
		
		temp = 0;
		for (int i = w - 1; i > max_h_index; i--) {
			if (heights[i] > temp) {
				temp = heights[i];
			}
			sum += temp;
		}
		
	
		for (int i = 0; i < w; i++) {
			sum -= heights[i];
		}
		
		System.out.println(sum);
	}

}
