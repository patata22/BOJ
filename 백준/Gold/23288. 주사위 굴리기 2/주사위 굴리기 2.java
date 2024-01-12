import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        GameBoard gameBoard = new GameBoard();
        System.out.println(gameBoard.playGame());
    }
}

class GameBoard{
    private int n,m;
    private int x=0,y=0;
    private int direction = 1;
    private int[] dx = new int[]{-1,0,1,0};
    private int[] dy = new int[]{0,1,0,-1};
    private int[][] board;
    private int[][] visited;
    private int moveCount;
    private HashMap<Integer, Integer> scoreBoard = new HashMap<>();
    private int score = 0;
    private Dice dice = new Dice();

    public GameBoard() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        this.n=Integer.parseInt(s[0]);
        this.m=Integer.parseInt(s[1]);
        this.moveCount=Integer.parseInt(s[2]);
        board = new int[n][m];
        visited= new int[n][m];

        for(int i=0;i<n;i++){
            s = br.readLine().split(" ");
            for(int j=0;j<m;j++){
                board[i][j] = Integer.parseInt(s[j]);
            }
        }
        initScoreBoard();
    }

    private void initScoreBoard(){
        int unused=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(visited[i][j]==0){
                    travel(i,j,++unused);
                }
            }
        }
    }

    private void travel(int x, int y, int order){
        Queue<int[]> q = new ArrayDeque<>();
        int num = board[x][y];
        int count=1;
        q.add(new int[]{x,y});
        visited[x][y]=order;
        while(!q.isEmpty()){
            x=q.peek()[0];
            y=q.poll()[1];
            for(int i=0;i<4;i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                if(0<=nx&&nx<n&&0<=ny&&ny<m&&board[nx][ny]==num&&visited[nx][ny]==0){
                    q.add(new int[]{nx,ny});
                    visited[nx][ny]=order;
                    count++;
                }
            }
        }
        scoreBoard.put(order, count);
    }


    private void RollDice(){
        int nx = x+dx[direction];
        int ny = y+dy[direction];
        if(!(0<=nx&&nx<n&&0<=ny&&ny<m)){
            direction = (direction+2)%4;
            nx = x+dx[direction];
            ny = y+dy[direction];
        }
        x=nx;
        y=ny;
        dice.roll(direction);
        score+=calcScore();
        setDirection();
    }

    private int calcScore(){
        int space = scoreBoard.get(visited[x][y]);
        int num = board[x][y];

        return space*num;
    }
    private void setDirection(){
        int bottom = dice.getBottom();
        int num = board[x][y];
        if(bottom>num){
            direction = (direction+1)%4;
        }else if(bottom<num){
            direction = (direction+3)%4;
        }
    }

    public int playGame(){
        for(int i=0;i<moveCount;i++){
            RollDice();
        }
        return score;
    }
}

class Dice{
    private int up=1;
    private int bottom=6;
    private int front=5;
    private int back=2;
    private int left=4;
    private int right=3;

    private void rollNorth(){
        int temp = up;
        up=front;
        front=bottom;
        bottom=back;
        back=temp;
    }

    private void rollSouth(){
        int temp=up;
        up=back;
        back=bottom;
        bottom=front;
        front=temp;
    }

    private void rollEast(){
        int temp=up;
        up=left;
        left=bottom;
        bottom=right;
        right=temp;
    }

    private void rollWest(){
        int temp=up;
        up=right;
        right=bottom;
        bottom=left;
        left=temp;
    }

    public void roll(int direction){
        if(direction==0){
            rollNorth();
        }else if(direction==1){
            rollEast();
        }else if(direction==2){
            rollSouth();
        }else if(direction==3){
            rollWest();
        }
    }

    public int getBottom() {
        return bottom;
    }
}