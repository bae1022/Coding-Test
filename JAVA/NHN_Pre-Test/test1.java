package nhn_practice;
import java.util.*;

class Field{
	private int x;
	private int y;

	public Field(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return this.x;
	}

	public int getY() {
		return this.y;
	}
}

public class test1 {

	static int n;

	static int bfs(int[][] field, Field f) {
		Queue<Field> q = new LinkedList<>();

		q.offer(f);

		int dx[] = {0, 0, -1, 1};
		int dy[] = {-1, 1, 0, 0};

		int cnt = 0;
		
		while(!q.isEmpty()) {
			Field ff = q.poll();

			int x = ff.getX();
			int y = ff.getY();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
					continue;
				}
				else {
					if (field[nx][ny] == 1){
						field[nx][ny] = 0;
						q.offer(new Field(nx, ny));
						cnt += 1;
					}
				}
			}
		}


		return cnt;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();

		int[][] field = new int[n][n];


		for (int i = 0; i < n; i++) {
			String input = sc.next();
			for (int j = 0; j < n; j++) {
				field[i][j] = input.charAt(j) - '0';
			}
		}

		Field f;

		int max = -1;
		int temp = 0;
		
		int cnt = 0;
		
		ArrayList<Integer> answer_list = new ArrayList<Integer>();
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (field[i][j] == 1) {
					
					f = new Field(i, j);
					temp = bfs(field, f);
					
					cnt += 1;
					
					answer_list.add(temp);
				}
			}
		}
		

		System.out.println(cnt);
		
		Collections.sort(answer_list);
		for (Integer i : answer_list) {
			System.out.print(i + " ");
		}

	}

}
