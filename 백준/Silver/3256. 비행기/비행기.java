import java.util.Scanner;

public class Main{

    static int n;
    static Passenger[] passengers;
    static boolean[] aisle;

    static int sol(){
        int answer=-1;
        while(true){
            answer++;
            int cnt=0;
            for (Passenger passenger : passengers) {
                move(passenger);
                if(passenger.arrive) cnt++;
            }
            if(cnt==n) break;
        }

        return answer;
    }

    static void move(Passenger passenger){
        if(passenger.arrive) return;

        if(passenger.now==passenger.row){
            if(passenger.cargo==4){
                passenger.arrive=true;
                aisle[passenger.row]=false;
            }else{
                passenger.cargo++;
            }
        }else{
            if(!aisle[passenger.now+1]){
                aisle[passenger.now+1]=true;
                aisle[passenger.now]=false;
                passenger.now++;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        passengers=new Passenger[n];
        for(int i=0;i<n;i++){
            passengers[i]=new Passenger(sc.nextInt());
        }
        aisle=new boolean[1001];
        System.out.println(sol());
    }
}

class Passenger{
    int now=0;
    int row;
    boolean arrive=false;
    int cargo=0;

    public Passenger(int row) {
        this.row = row;
    }
}

