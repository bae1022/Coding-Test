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
//class Dot{ // X,Y 좌표를 저장하는 클래스
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
//  	static int dx[] = {1,-1,0,0}; // 상, 하, 좌, 우를 탐색하기 위한 배열
//    static int dy[] = {0,0,1,-1};
//    
//    // BFS 탐색 메소드
//	static void bfs(int[][] a, boolean[][] check, Dot d) {
//    	// 전달받은 좌표부터 주변의 집 좌표를 저장 할 큐
//		Queue<Dot> q = new LinkedList<>();
//		int cnt = 0; // 주변에 존재하는 집의 수를 저장 할 변수
//		
//		q.offer(d); // 초기 전달받은 좌표를 큐에 우선 삽입
//		check[d.getX()][d.getY()] = true; // 해당 좌표 방문 표시
//		
//		while(!q.isEmpty()) { // 주변의 집이 존재하지 않을 때 까지 반복
//			Dot d_p = q.poll(); // 전달받은 좌표 값
//			int x = d_p.getX();
//			int y = d_p.getY();
//			cnt++; // 주변 집의 수만큼 반복되므로 cnt 증가
//			
//			for(int i=0;i<4;i++) { // 상, 하, 좌, 우 탐색
//            	// 각 값의 계산에 따라 상, 하, 좌, 우의 좌표가 저장되며 반복
//				int nx = x + dx[i]; 
//				int ny = y + dy[i];
//				
//                // 맵의 범위를 벗어나는 좌표는 무시
//				if(nx>=a.length || nx<0 || ny>=a[nx].length || ny < 0) continue;
//				
//                // 이미 방문한 적 있는 집은 무시
//				if(check[nx][ny]) continue;
//				
//                // 상, 하, 좌, 우에 집이 존재하는 경우
//				if( a[nx][ny] == 1){					
//					check[nx][ny] = true; // 방문처리 후
//					q.offer(new Dot(nx,ny)); // 해당 집의 좌표를 큐에 넣어준 뒤 계속해서 탐색
//				}
//			}			
//		}
//		
//        // 모든 과정이 끝나면 주변에 더 이상 방문하지 않은 집이 없다는 의미로 ArrayList에 집의 수를 삽입
//		count.add(cnt); 
//		
//	}
//	
//	public static void main(String[] args)  {
//		Scanner in = new Scanner(System.in);
//		
//		int n = in.nextInt(); // 맵의 크기
//		int a[][] = new int[n][n]; // N X N 크기의 맵
//		boolean check[][] = new boolean[n][n]; // N X N 크기의 방문여부 배열
//		
//		for(int i=0;i<a.length;i++) { // 단지 정보 입력
//			String str = in.next();
//			for(int j=0;j<a[i].length;j++) {
//				a[i][j] = str.charAt(j)-'0';
//			}
//		}
//		
//		Dot d; // BFS 탐색을 시작할 위치 정보를 담을 객체
//		
//		for(int i=0;i<a.length;i++) {			
//			for(int j=0;j<a[i].length;j++) {
//				if(a[i][j] == 1 && check[i][j] == false) { // 맵을 탐색하다 단지가 위치하면서 방문하지 않았다면
//					d = new Dot(i,j); // 좌표 정보 객체를 생성해
//					bfs(a,check,d); // 해당 좌표부터 너비 우선 탐색을 수행
//				}
//			}
//		}
//		
//		System.out.println(count.size()); // 각 단지의 수는 ArrayList의 size
//		Collections.sort(count); // 오름차순 출력을 위한 정렬
//		for(int i =0; i<count.size();i++) { // 각 단지의 집 수를 출력
//			System.out.println(count.get(i));
//		}
//		
//	  }
//}