package _8911;

import java.util.*;
public class _8911 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
			
		int[] dx = {0, -1, 0, 1}; // ºÏ, ¼­, ³², µ¿
		int[] dy = {1, 0, -1, 0};	

		for (int i = 0; i < t; i++) {
			int max_pos_x = 0;
			int max_pos_y = 0;
			
			int min_pos_x = 0;
			int min_pos_y = 0;
			
			int pos_x = 0;
			int pos_y = 0;
			
			int turtle = 0; //ºÏ, ¼­, ³², µ¿
			
			String s = sc.next();

			String[] ss = s.split("");

			for (int j = 0; j < ss.length; j++) {
				if (ss[j].equals("F")) {
					pos_x = pos_x + dx[turtle];
					pos_y = pos_y + dy[turtle];
					
					if (pos_x > max_pos_x) {
						max_pos_x = pos_x;
					}
					
					if (pos_x < min_pos_x) {
						min_pos_x = pos_x;
					}
					
					if (pos_y > max_pos_y) {
						max_pos_y = pos_y;
					}
					
					if (pos_y < min_pos_y) {
						min_pos_y = pos_y;
					}
				}
				else if (ss[j].equals("B")){
					pos_x = pos_x - dx[turtle];
					pos_y = pos_y - dy[turtle];
					
					if (pos_x > max_pos_x) {
						max_pos_x = pos_x;
					}
					
					if (pos_x < min_pos_x) {
						min_pos_x = pos_x;
					}
					
					if (pos_y > max_pos_y) {
						max_pos_y = pos_y;
					}
					
					if (pos_y < min_pos_y) {
						min_pos_y = pos_y;
					}
				}
				else if (ss[j].equals("L")){
					if (turtle == 3) {
						turtle = 0;
					}
					else {
						turtle += 1;
					}
				}
				else if (ss[j].equals("R")){
					if (turtle == 0) {
						turtle = 3;
					}
					else {
						turtle -= 1;
					}
				}
			}
			
			System.out.println(Math.abs((max_pos_x - min_pos_x) * (max_pos_y - min_pos_y)));
		}
	}

}
