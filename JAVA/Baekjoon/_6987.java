package _6987;

import java.util.*;
public class _6987 {
	static int[] ans;
	static int[][] result;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ans = new int[4];
		Scanner sc = new Scanner(System.in);
		
		
		for(int i = 0; i < 4; i++) {
            String[] input = sc.nextLine().split(" ");
            
            result = new int[6][3];
            
            int sum = 0;

            for(int j = 0; j < 18; j++) {
                int x = Integer.parseInt(input[j]);
                
                
                result[j / 3][j % 3] = x;
                sum += x;

            }

            if(sum!=30)
                continue;

            dfs(0, 1, i);
        }
		
		for (int i = 0; i < 4; i++) {
			System.out.print(ans[i] + " ");
		}
	}
	
	public static void dfs(int a, int b, int c) {
		if (a == 6) {
			ans[c] = 1;
		}
		
		else if (b == 6) {
			dfs(a + 1, a + 2, c);
		}
		
		else {
			for (int i = 0; i < 3; i++) {
				if (result[a][i] >= 1 && result[b][2 - i] >= 1) {
					result[a][i]--;
					result[b][2 - i]--;
					
					dfs(a, b + 1, c);
					
					result[a][i]++;
					result[b][2 - i]++;
				}
			}
		}
	}

}
