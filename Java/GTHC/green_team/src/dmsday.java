import java.util.Scanner;

public class dmsday {
    
    public static int doomsday(int year){

        //considerando https://pt.wikipedia.org/wiki/Algoritmo_Doomsday como somente anos do século 21
        //considering https://en.wikipedia.org/wiki/Doomsday_rule as only years in the 21th century
        //considerando https://it.wikipedia.org/wiki/Algoritmo_Doomsday come solo anni nel secolo 21
        int d_sem = 0;

        if(year % 2 == 0){

            year = year / 2;

            if(year % 2 == 0){

                year = year % 7;
                d_sem = 7 - year;

            }
            else{

                year = year + 11;
                year = year % 7;
                d_sem = 7 - year;

            }

        }
        else{

            year = year + 11;
            year = year / 2;

            if(year % 2 == 0){

                year = year % 7;
                d_sem = 7 - year;
                d_sem = (d_sem + 3) - 7;

            }
            else{

                year = year + 11;
                year = year % 7;
                d_sem = 7 - year;
                d_sem = (d_sem + 3) - 7;

            }

        }
        
        //dia ancora sai no return como 1=domingo, 2=segunda, 3=terça, 4=quarta, 5=quinta, 6=sexta, 7=sabado
        //anchor day returns as 1=sunday, 2=monday, 3=tuesday, 4=wednesday, 5=thursday, 6=friday, 7=saturday
        //giorno ancora ritorna come 1=domenico, 2=lunedi, 3=martedi, 4=mercioledi, 5=giovedi, 6=venerdi, 7=sabato
        return d_sem;

    }

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        System.out.println(doomsday(n));

        sc.close();

    }

}
