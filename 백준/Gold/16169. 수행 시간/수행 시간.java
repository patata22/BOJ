import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static int n;
    static int maxLevel = 0;
    static ArrayList<Computer>[] computers;


    public static int solve(){
        for(int i=1;i<maxLevel;i++){
            for (Computer computer : computers[i]) {
                for (Computer nxtComputer : computers[i + 1]) {
                    nxtComputer.calcStartTime(computer);
                }
            }
        }

        int answer=0;
        for (Computer computer : computers[maxLevel]) {
            answer=Math.max(answer,computer.startTime+ computer.executeTime);
        }
        return answer;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        computers = new ArrayList[n+1];
        for(int i=1;i<n+1;i++){
            computers[i] = new ArrayList<>();
        }
        for(int i=0;i<n;i++){
            int level = sc.nextInt();
            maxLevel = Math.max(maxLevel, level);
            int executeTime = sc.nextInt();
            Computer computer = new Computer(i,level, executeTime);
            computers[level].add(computer);
        }

        System.out.println(solve());
    }
}

class Computer{
    int idx;
    int level;
    int startTime;
    int executeTime;

    public Computer(int idx, int level, int executeTime) {
        this.idx = idx;
        this.startTime = 0;
        this.level = level;
        this.executeTime = executeTime;
    }

    public void calcStartTime(Computer computer){
        int temp = (computer.idx-this.idx)*(computer.idx-this.idx)+computer.startTime+computer.executeTime;
        this.startTime = Math.max(temp, this.startTime);
    }
}