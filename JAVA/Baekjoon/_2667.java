package _2667;
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

public class _2667 {
	static int n;

	static int bfs(int[][] field, Field f) {
		Queue<Field> q = new LinkedList<>();

		q.offer(f);

		int dx[] = {0, 0, -1, 1};
		int dy[] = {-1, 1, 0, 0};

		int cnt = 0;

		while (!q.isEmpty()) {
			Field ff = q.poll();

			int x = ff.getX();
			int y = ff.getY();
			
			field[x][y] = 0;
			cnt++;
			
			System.out.println(".." + x + y + cnt);

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
					continue;
				}
				else {
					if (field[nx][ny] != 0){
						q.offer(new Field(nx, ny));
						field[nx][ny] = 0;
						
					}
					else {
						continue;
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
		
		Field f;

		for (int i = 0; i < n; i++) {
			String s = sc.next();

			String[] array = s.split("");

			for (int j = 0; j < n; j++) {
				field[i][j] = Integer.parseInt(array[j]);
			}
		}
		
		ArrayList<Integer> answer_list = new ArrayList<Integer>();
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (field[i][j] != 0) {
					f = new Field(i, j);
					int answer = bfs(field, f);
					
					answer_list.add(answer);
				}
			}
		}

		
		Collections.sort(answer_list);
		System.out.println(answer_list.size());
		
		for (int i = 0; i < answer_list.size(); i++){
			System.out.println(answer_list.get(i));
		}
	}


}
//package _2667;
//import java.util.ArrayList;
//import java.util.Collections;
//import java.util.LinkedList;
//import java.util.Queue;
//import java.util.Scanner;
//
//class Dot{ // X,Y ��ǥ�� �����ϴ� Ŭ����
//		int x;
//		int y;
//		
//		public Dot(int x, int y) {
//			super();
//			this.x = x;
//			this.y = y;
//		}
//		
//		public int getX() {
//			return x;
//		}
//		public void setX(int x) {
//			this.x = x;
//		}
//		public int getY() {
//			return y;
//		}
//		public void setY(int y) {
//			this.y = y;
//		}				
//}
//
//class _2667 {
//  
//  	static ArrayList<Integer> count = new ArrayList<>();
//  	static int dx[] = {1,-1,0,0}; // ��, ��, ��, �츦 Ž���ϱ� ���� �迭
//    static int dy[] = {0,0,1,-1};
//    
//    // BFS Ž�� �޼ҵ�
//	static void bfs(int[][] a, boolean[][] check, Dot d) {
//    	// ���޹��� ��ǥ���� �ֺ��� �� ��ǥ�� ���� �� ť
//		Queue<Dot> q = new LinkedList<>();
//		int cnt = 0; // �ֺ��� �����ϴ� ���� ���� ���� �� ����
//		
//		q.offer(d); // �ʱ� ���޹��� ��ǥ�� ť�� �켱 ����
//		check[d.getX()][d.getY()] = true; // �ش� ��ǥ �湮 ǥ��
//		
//		while(!q.isEmpty()) { // �ֺ��� ���� �������� ���� �� ���� �ݺ�
//			Dot d_p = q.poll(); // ���޹��� ��ǥ ��
//			int x = d_p.getX();
//			int y = d_p.getY();
//			cnt++; // �ֺ� ���� ����ŭ �ݺ��ǹǷ� cnt ����
//			
//			for(int i=0;i<4;i++) { // ��, ��, ��, �� Ž��
//            	// �� ���� ��꿡 ���� ��, ��, ��, ���� ��ǥ�� ����Ǹ� �ݺ�
//				int nx = x + dx[i]; 
//				int ny = y + dy[i];
//				
//                // ���� ������ ����� ��ǥ�� ����
//				if(nx>=a.length || nx<0 || ny>=a[nx].length || ny < 0) continue;
//				
//                // �̹� �湮�� �� �ִ� ���� ����
//				if(check[nx][ny]) continue;
//				
//                // ��, ��, ��, �쿡 ���� �����ϴ� ���
//				if( a[nx][ny] == 1){					
//					check[nx][ny] = true; // �湮ó�� ��
//					q.offer(new Dot(nx,ny)); // �ش� ���� ��ǥ�� ť�� �־��� �� ����ؼ� Ž��
//				}
//			}			
//		}
//		
//        // ��� ������ ������ �ֺ��� �� �̻� �湮���� ���� ���� ���ٴ� �ǹ̷� ArrayList�� ���� ���� ����
//		count.add(cnt); 
//		
//	}
//	
//	public static void main(String[] args)  {
//		Scanner in = new Scanner(System.in);
//		
//		int n = in.nextInt(); // ���� ũ��
//		int a[][] = new int[n][n]; // N X N ũ���� ��
//		boolean check[][] = new boolean[n][n]; // N X N ũ���� �湮���� �迭
//		
//		for(int i=0;i<a.length;i++) { // ���� ���� �Է�
//			String str = in.next();
//			for(int j=0;j<a[i].length;j++) {
//				a[i][j] = str.charAt(j)-'0';
//			}
//		}
//		
//		Dot d; // BFS Ž���� ������ ��ġ ������ ���� ��ü
//		
//		for(int i=0;i<a.length;i++) {			
//			for(int j=0;j<a[i].length;j++) {
//				if(a[i][j] == 1 && check[i][j] == false) { // ���� Ž���ϴ� ������ ��ġ�ϸ鼭 �湮���� �ʾҴٸ�
//					d = new Dot(i,j); // ��ǥ ���� ��ü�� ������
//					bfs(a,check,d); // �ش� ��ǥ���� �ʺ� �켱 Ž���� ����
//				}
//			}
//		}
//		
//		System.out.println(count.size()); // �� ������ ���� ArrayList�� size
//		Collections.sort(count); // �������� ����� ���� ����
//		for(int i =0; i<count.size();i++) { // �� ������ �� ���� ���
//			System.out.println(count.get(i));
//		}
//		
//	  }
//}