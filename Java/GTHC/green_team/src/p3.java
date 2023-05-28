import java.util.Scanner;

public class p3 {
    
    public static void main(String[] args) throws Exception {
   	 
        Scanner sc = new Scanner(System.in);
    	  int N = sc.nextInt();
    	  int c = 1;
    	  int sp = (N * 2) - 1;
    	  int alt_sp = (N * 2) - sp;

    	  for(int i = 0; i < N; i++){
       	 
            String temp_s = "";
        	for(int j = 0; j < sp - 1; j++){

                temp_s += " ";

        	}
        	for(int x = 0; x < alt_sp; x++){

                temp_s += Integer.toString(c) + " ";
           	    c++;

        	}
        	alt_sp++;
        	sp -= 2;
            
            //lines after N = 4 are not aligned
            //linhas apos N = 4 nao estao alinhadas
            //linjer efter N = 4 er ikke justert
        	System.out.println(temp_s);

        }
        
        sc.close();
   	 
    }

}

