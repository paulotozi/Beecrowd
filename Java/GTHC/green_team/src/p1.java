import java.util.Scanner;

public class p1 {
    
    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);
        String dot = "* ";
        int N = sc.nextInt();

        for(int i = 0; i < N; i++){

            System.out.println(dot);
            dot += "* ";
        
        sc.close();
        }
    }

}
