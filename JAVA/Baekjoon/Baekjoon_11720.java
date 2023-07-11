package Baekjoon_11720;

import java.util.Scanner;

public class Baekjoon_11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String sNum = sc.next();

        char[] cNum = sNum.toCharArray();

        int answer = 0;

        for (int i = 0; i < n; i++){
            answer += cNum[i] - '0';
            // char 형으로 받아왔기 때문에 '0'(48) 빼줘야 숫자로 인식 가능
        }

        System.out.println(answer);
    }
}
