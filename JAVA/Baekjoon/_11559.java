package _11559;

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
public class _11559 {

	static char[][] field;
	static boolean flag = true;

	static int answer = 0;

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);

		field = new char[12][6];

		for (int i = 0; i < 12; i++) {
			String row = "";

			row = sc.nextLine();

			for (int j = 0; j < 6; j++) {
				field[i][j] = row.charAt(j);
			}
		}

		Field f;	

		while(true) {
			flag = true;        // 4개 이상의 뿌요를 못터트리면 게임을 종료시키는 flag

			for(int i=0; i<12; i++) {
				for(int j=0; j<6; j++) {
					if(field[i][j] != '.') {    
						String color = Character.toString(field[i][j]);

						f = new Field(i, j);
						bfs(f, color);

					}
				}
			}

			down();

			if(flag) {
				break;
			}
			answer++;
		}

		System.out.println(answer);

	}

	public static void bfs(Field f, String color) {
		Queue<Field> q = new LinkedList<>();

		q.offer(f);

		int dx[] = {0, 0, -1, 1};
		int dy[] = {-1, 1, 0, 0};

		ArrayList<Integer> array_x = new ArrayList<>();
		ArrayList<Integer> array_y = new ArrayList<>();

		int cnt = 0;

		while (!q.isEmpty()) {
			Field ff = q.poll();

			int x = ff.getX();
			int y = ff.getY();

			field[x][y] = '.';

			array_x.add(x);
			array_y.add(y);

			cnt ++;

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= 12 || ny < 0 || ny >= 6) {
					continue;
				}
				else {
					String n = Character.toString(field[nx][ny]);
					if (!n.equals(color)) {
						continue;
					}
					else {
						q.offer(new Field(nx, ny));

						field[nx][ny] = '.';

						array_x.add(nx);
						array_y.add(ny);
					}
				}
			}	
		}

		if (cnt < 4) { // 붙어있는 게 4개보다 적다.
			for (int i = 0; i < array_x.size(); i++) {
				int t_x = array_x.get(i);
				int t_y = array_y.get(i);

				field[t_x][t_y] = color.charAt(0);
			}
		}
		else { // 뿌요 터짐
			flag = false;

		}
	}
	
	public static void down() { //뿌요들을 아래로
		for (int i = 0; i < 6; i++) {
			for (int j = 12 - 1; j > 0; j--) {
				if (field[j][i] == '.') {
					for (int k = j - 1; k >= 0; k--) {
						if (field[k][i] != '.') {
							field[j][i] = field[k][i];
							field[k][i] = '.';

							break;
						}
					}
				}
			}
		}
	}

}
