package com.example.helloworld;

import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int ceva = scanner.nextInt();

        scanner.close();
        if(ceva > 0) {
            System.out.println("e pozitiv");
        }
        else{
            if(ceva < 0){
                System.out.println("e negativ");
            }
            else{
                System.out.println("este 0");
            }
        }

    }
}
