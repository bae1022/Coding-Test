package _17070;

import java.util.*;
public class _17070 {
	
	static int n;
	static int answer = 0;
	static int[][] home;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		home = new int[n][n];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				home[i][j] = sc.nextInt();
			}
		}
		
		dfs(0, 1, 0);
		System.out.println(answer);
	}
	
	public static void dfs(int x, int y, int dir) {
		if (x == n - 1 && y == n - 1) {
			answer++;
			return;
		}
		
		if (dir == 0) { // 가로방향/ 가로, 대각 이동 가능
			if (y + 1 < n && home[x][y + 1] == 0) { // 가로
				dfs(x, y + 1, 0);
			}
			
			if (x + 1 < n && y + 1 < n && home[x + 1][y] == 0 && home[x][y + 1] == 0 && home[x + 1][y + 1] == 0) { //대각
				dfs(x + 1, y + 1, 2);
			}
		}
		
		else if (dir == 1) { // 세로방향/ 세로, 대각 이동 가능
			if (x + 1 < n && home[x + 1][y] == 0) {
				dfs(x + 1, y, 1);
			}
			
			if (x + 1 < n && y + 1 < n && home[x + 1][y] == 0 && home[x][y + 1] == 0 && home[x + 1][y + 1] == 0) { //대각
				dfs(x + 1, y + 1, 2);
			}
		}
		
		else if (dir == 2) {
			if (y + 1 < n && home[x][y + 1] == 0) { // 가로
				dfs(x, y + 1, 0);
			}
			if (x + 1 < n && home[x + 1][y] == 0) {
				dfs(x + 1, y, 1);
			}
			if (x + 1 < n && y + 1 < n && home[x + 1][y] == 0 && home[x][y + 1] == 0 && home[x + 1][y + 1] == 0) { //대각
				dfs(x + 1, y + 1, 2);
			}
		}

	}

}
