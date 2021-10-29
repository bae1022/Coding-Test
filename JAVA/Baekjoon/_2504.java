package _2504;

import java.util.*;
public class _2504 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);

		String s = sc.nextLine();
		String[] ss = s.split("");

		Stack<String> stack = new Stack<>();

		int cnt1 = 0; // (의 개수, ) 나오면 차감
		int cnt2 = 0; // [의 개수, ] 나오면 차감
		int state = 0;

		for (int i = 0; i < ss.length; i++) {
			if (cnt1 < 0 || cnt2 < 0) {
				state = -1;
				
				break;
			}
			
			if (ss[i].equals("(")) {
				cnt1++;
			}

			else if (ss[i].equals(")")){
				cnt1--;
			}

			else if (ss[i].equals("[")){
				cnt2++;
			}

			else if (ss[i].equals("]")) {
				cnt2--;
			}
		}

		if (cnt1 != 0 || cnt2 != 0 || state == -1) {
			System.out.println(0);
		}
		
		else {
			for (int i = 0; i < ss.length; i++) {
				if (state == -1) {
					break;
				}
				if (ss[i].equals("(") || ss[i].equals("[")) {
					stack.add(ss[i]);

				}

				else if (ss[i].equals(")")){
					
					ArrayList<String> list = new ArrayList<>();
					
					while (true) {
						String t = stack.peek();

						if (t.equals("(")) {
							stack.pop();
							break;
						}
						else {
							String temp = stack.pop();
							
							if (temp.equals("(") || temp.equals(")") || temp.equals("[") || temp.equals("]")){
								state = -1;
								break;
							}
							list.add(temp);
						}	
					}

					if (list.size() >= 2) {
						int sum = 0;
						
						for (int j = 0; j < list.size(); j++){
							sum += Integer.parseInt(list.get(j));
						}
						
						stack.push(String.valueOf(2 * sum));
					}
					
					else if (list.size() == 1){
						int sum = 0;
						
						sum = 2 * Integer.parseInt(list.get(0));
						stack.push(String.valueOf(sum));
					}
					
					else if (list.size() == 0) {
						stack.push("2");
						
					}
				}

				else if (ss[i].equals("]")) {
					
					ArrayList<String> list = new ArrayList<>();
					
					while (true) {
						String t = stack.peek();

						if (t.equals("[")) {
							stack.pop();
							break;
						}
						else {
							String temp = stack.pop();
							
							if (temp.equals("(") || temp.equals(")") || temp.equals("[") || temp.equals("]")){
								state = -1;
								break;
							}
							
							list.add(temp);
						}	
					}

					if (list.size() >= 2) {
						int sum = 0;
						
						for (int j = 0; j < list.size(); j++){
							
							sum += Integer.parseInt(list.get(j));
						}
						
						stack.push(String.valueOf(3 * sum));	
					}
					
					else if (list.size() == 1){
						int sum = 0;
						
						sum = 3 * Integer.parseInt(list.get(0));
						stack.push(String.valueOf(sum));
						
					}
					
					else if (list.size() == 0) {
						stack.push("3");
						
					}
				}

			}
			
			int answer = 0;
			
			if (state == -1) {
				System.out.println(0);
			}
			else {
				while (!stack.isEmpty()) {
					answer += Integer.parseInt(stack.pop());
				}
				
				System.out.println(answer);
			}
			
			
			
		}
	}
}
