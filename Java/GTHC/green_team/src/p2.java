import java.util.Scanner;
import java.util.Arrays;

public class p2 {
    
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[] numbers = new String[N];
        String temp_s = "";
        int i = 0;

        for(i = 0; i < N; i++){

            numbers[i] = Integer.toString(i + 1) + " ";
            
        }

        for(int j = 0; j < N; j++){
            
            System.out.print(temp_s);
            Arrays.asList(numbers).forEach(number->System.out.print(String.format("%s ", number)));
            numbers[j] = " ";
            temp_s += " ";
            System.out.print("\n"); 
        sc.close();    
        }
        

    }

}
