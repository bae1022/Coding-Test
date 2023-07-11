package Baekjoon_11659;

import java.util.ArrayList;
import java.util.Scanner;

public class Baekjoon_11659 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n_data = sc.nextInt();
        int n_answer = sc.nextInt();

        ArrayList<Integer> array = new ArrayList<>();
        ArrayList<Integer> sum_array = new ArrayList<>();

        int total = 0;
        sum_array.add(0);
        for (int i = 0; i < n_data; i++){
            int temp = sc.nextInt();
            total += temp;

            array.add(temp);
            sum_array.add(total);
        }

        for (int i = 0; i < n_answer; i++){
            int start = sc.nextInt();
            int end = sc.nextInt();

            System.out.println(sum_array.get(end) - sum_array.get(start - 1));
        }
    }
}
