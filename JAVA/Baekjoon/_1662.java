package _1662;

import java.util.*;
import java.io.*;
public class _1662 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		String s = sc.next();
		String[] ss = s.split("");

		Stack<String> stack = new Stack<>();

		for (int i = 0; i < ss.length; i++) {
			if (!ss[i].equals(")")) {
				stack.push(ss[i]);
				System.out.println(ss[i]);
			}
			else {
				int cnt = 0;

				while(!stack.peek().equals("(")) {
					String output = stack.pop();

					if (output.equals("*")) {
						int len = Integer.parseInt(stack.pop());
						cnt += len;
					}
					else {
						cnt += 1;
					}
				}

				stack.pop(); //"("제거

				//				System.out.println(stack.peek());
				int len = Integer.parseInt(stack.pop());
				cnt *= len;
				stack.push(String.valueOf(cnt));
				stack.push("*"); // * 밑에 있는 숫자는 문자열이 아닌 숫자의 길이
			}
		}

		int answer = 0;
		while (!stack.isEmpty()) {
			if (stack.peek().equals("*")) {
				stack.pop();
				answer += Integer.parseInt(stack.pop());
			}
			else {
				stack.pop();
				answer += 1;
			}
		}

		System.out.println(answer);
	}
	

}