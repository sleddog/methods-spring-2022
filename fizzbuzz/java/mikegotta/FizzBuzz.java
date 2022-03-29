import java.util.ArrayList;

////  Welcome to FizzBuzz, this program takes an integer as a   ////
////  commandline argument and runs that integer searching for  ////
////  divisible integers by 3, 5, and 15 and prints             ////
////  Fizz, Buzz, and FizzBuzz respectively.                    ////

public class FizzBuzz {

    public static void fizzBuzz(int number){
        int step = 1;
        ArrayList<String> printToConsole = new ArrayList<>();
        while (step <= number){
            if (step%15 == 0){
                printToConsole.add("FizzBuzz");
            }
            else if (step%5 == 0 ){
                printToConsole.add("Buzz");
            }
            else if (step%3 ==0 ){
                printToConsole.add("Fizz");
            }
            else{
                printToConsole.add(String.valueOf(step));
            }
            step++;
        }
        printFizzBuzz(printToConsole);
    }

    public static void printFizzBuzz(ArrayList<String> printing){
        for (String s : printing) {
            System.out.println(s);
        }
    }

    public static void main(String[] args) {
	int number = Integer.parseInt(args[0]);
        fizzBuzz(number);
    }
}
