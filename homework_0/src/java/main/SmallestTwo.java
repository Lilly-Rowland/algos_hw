import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class SmallestTwo {
    public static void main(String[] args) {
        Set<Integer> numbers = new HashSet<>();
        try (Scanner scanner = new Scanner(System.in)){
        //reading int the input
        while (scanner.hasNextInt()) {
            numbers.add(scanner.nextInt());
            }
        }

        //have a minimum variable and second minimum vairable
        int min = Integer.MAX_VALUE;
        int second_min = Integer.MAX_VALUE;

        for (int number : numbers) {
            if (number < min) {
                second_min = min;
                min = number;
            }
            else if (number < second_min) second_min = number;
        }

        //proitning out the min and second min
        System.out.println(min);
        System.out.println(second_min);

    }
        
    }
