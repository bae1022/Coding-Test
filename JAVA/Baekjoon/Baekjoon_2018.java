package Main;

import java.util.Arrays;
import java.util.Scanner;

public class Baekjoon_2018 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int sum = 1;
        int start_index = 1;
        int end_index = 1;

        int answer = 1; // 자기 자신은 기포함

        while (n != end_index)
        {
            if (sum == n){
                answer++;
                end_index++;

                sum += end_index;
            }

            else if (sum > n){
                sum -= start_index;
                start_index++;
            }

            else if (sum < n){
                end_index++;
                sum += end_index;
            }
        }

        System.out.println(answer);

    }
}
