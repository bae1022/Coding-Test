package Baekjoon_1546;

import java.util.ArrayList;
import java.util.Scanner;

public class Baekjoon_1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArrayList<Integer> n_list = new ArrayList<>();

        double n_max = 0;

        for (int i = 0; i < n; i ++){
            int num = sc.nextInt();

            if (n_max < num){
                n_max = num;
            }

            n_list.add(num);
        }

        double total = 0;
        for (int i = 0; i < n_list.size(); i ++){
            double temp = n_list.get(i) / n_max * 100;

            total += temp;
        }

        System.out.println(total / n);
    }
}
