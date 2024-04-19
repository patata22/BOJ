import java.util.Scanner;

public class Main {
    
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int n,m,t,up,down;
    static int[][] board;

    private static void init() {
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        t=sc.nextInt();
        board= new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                int x=sc.nextInt();
                if(x==-1){
                    if(up==0) up=i;
                    else down=i;
                }
                board[i][j]=x;
            }
        }
    }

    private static void spread(){
        int[][] nextBoard = new int[n][m];
        for(int x=0;x<n;x++){
            for(int y=0;y<m;y++){
                if(board[x][y]==-1){
                    nextBoard[x][y]=-1;
                    continue;
                }
                int total = board[x][y];
                int amount=board[x][y]/5;
                for(int i=0;i<4;i++){
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(0<=nx&&nx<n&&0<=ny&&ny<m&&board[nx][ny]!=-1){
                        nextBoard[nx][ny]+=amount;
                        total-=amount;
                    }
                }
                nextBoard[x][y]+=total;
            }
        }
        board = nextBoard;
    }

    private static void windUp(){
        int x = up-1;
        int y = 0;
        while(x>0){
            board[x][y]=board[x-1][y];
            x-=1;
        }
        while(y<m-1){
            board[x][y]=board[x][y+1];
            y+=1;
        }
        while(x<up){
            board[x][y]=board[x+1][y];
            x+=1;
        }
        while(y>1){
            board[x][y]=board[x][y-1];
            y-=1;
        }
        board[x][y]=0;
    }

    private static void windDown(){
        int x = down+1;
        int y= 0;
        while(x<n-1){
            board[x][y]=board[x+1][y];
            x+=1;
        }
        while(y<m-1){
            board[x][y]=board[x][y+1];
            y+=1;
        }
        while(x>down){
            board[x][y]=board[x-1][y];
            x-=1;
        }
        while(y>1){
            board[x][y]=board[x][y-1];
            y-=1;
        }
        board[x][y]=0;
    }

    private static void playTurn(){
        spread();
        windUp();
        windDown();
    }

    private static int getResult(){
        int answer=2;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                answer+=board[i][j];
            }
        }
        return answer;
    }
    
    public static void main(String[] args) {
        init();
        for(int i=0;i<t;i++){
            playTurn();
        }
        System.out.println(getResult());
    }
}