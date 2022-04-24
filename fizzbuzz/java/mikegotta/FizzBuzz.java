/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fizzbuzz;

////  Welcome to FizzBuzz, this program takes an integer as a   ////
////  commandline argument and runs that integer searching for  ////
////  divisible integers by 3, 5, 7, and 11 and prints          ////
////  Fizz, Buzz, Ping, and Pong respectively.                   ////

public class FizzBuzz {

    public static String fizzBuzz(int number){
        String output = "";
        if (number%3 ==0 ){
            output += "Fizz";
        }
        if (number%5 == 0 ){
            output += "Buzz";
        }
        if (number%7 ==0 ){
           output += "Ping";
        }
        if (number%11 ==0 ){
            output += "Pong";
        }
        if (output.equals("")){
            output += String.valueOf(number);
        }
        return output;
    }
    
    public void printFizzBuzz(String output){
        System.out.println(output);
    }

    public static void main(String[] args) {
        int number = Integer.parseInt(args[0]);
        FizzBuzz fb = new FizzBuzz();
        for (int i = 1; i <= number; i++){
            fb.printFizzBuzz(fb.fizzBuzz(i));
        }
    }
}