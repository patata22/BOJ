import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static int answer;
    public static void sol(int depth, Board board){
        if(depth==5){
            answer= Math.max(answer,board.getMax());
            return;
        }

        Board nxt = board.clone();
        nxt.moveRight();
        sol(depth+1, nxt);
        nxt = board.clone();
        nxt.moveLeft();
        sol(depth+1, nxt);
        nxt = board.clone();
        nxt.moveTop();
        sol(depth+1, nxt);
        nxt = board.clone();
        nxt.moveBottom();
        sol(depth+1, nxt);

    }


    public static void main(String[] args) throws IOException {
        answer=0;
        Board board = new Board();
        sol(0,board);
        System.out.println(answer);
    }

}

class Board{
    int n;
    int[][] blocks;

    public Board() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());
        blocks = new int[n][n];
        String[] temp;
        for(int i=0;i<n;i++){
            temp = br.readLine().split(" ");
            for(int j=0;j<n;j++){
                blocks[i][j]=Integer.parseInt(temp[j]);
            }
        }
    }

    public Board(Board b){
        n=b.n;
        blocks = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                blocks[i][j]=b.blocks[i][j];
            }
        }
    }

    public void moveRight(){
        boolean[][] merged = new boolean[n][n];
        for(int i=0;i<n;i++){
            for(int j=n-2;j>-1;j--){
                if(blocks[i][j]==0) continue;
                int y=j;
                while(y+1<n&&blocks[i][y+1]==0){
                    blocks[i][y+1]=blocks[i][y];
                    blocks[i][y]=0;
                    y++;
                }
                if(y+1<n&&blocks[i][y]==blocks[i][y+1]&&!merged[i][y+1]){
                    merged[i][y+1]=true;
                    blocks[i][y+1]*=2;
                    blocks[i][y]=0;
                }
            }
        }
    }

    public void moveLeft(){
        boolean[][] merged = new boolean[n][n];
        for(int i=0;i<n;i++){
            for(int j=1;j<n;j++){
                if(blocks[i][j]==0) continue;
                int y=j;
                while(y-1>=0&&blocks[i][y-1]==0){
                    blocks[i][y-1]=blocks[i][y];
                    blocks[i][y]=0;
                    y--;
                }
                if(y-1>=0&&blocks[i][y]==blocks[i][y-1]&&!merged[i][y-1]){
                    merged[i][y-1]=true;
                    blocks[i][y-1]*=2;
                    blocks[i][y]=0;
                }
            }
        }
    }

    public void moveTop(){
        boolean[][] merged = new boolean[n][n];
        for(int j=0;j<n;j++){
            for(int i=1;i<n;i++){
                if(blocks[i][j]==0) continue;
                int x=i;
                while(x-1>=0&&blocks[x-1][j]==0){
                    blocks[x-1][j]=blocks[x][j];
                    blocks[x][j]=0;
                    x--;
                }
                if(x-1>=0&&blocks[x][j]==blocks[x-1][j]&&!merged[x-1][j]){
                    merged[x-1][j]=true;
                    blocks[x-1][j]*=2;
                    blocks[x][j]=0;
                }
            }
        }
    }

    public void moveBottom(){
        boolean[][] merged = new boolean[n][n];
        for(int j=0;j<n;j++){
            for(int i=n-2;i>-1;i--){
                if(blocks[i][j]==0) continue;
                int x=i;
                while(x+1<n&&blocks[x+1][j]==0){
                    blocks[x+1][j]=blocks[x][j];
                    blocks[x][j]=0;
                    x++;
                }
                if(x+1<n&&blocks[x][j]==blocks[x+1][j]&&!merged[x+1][j]){
                    merged[x+1][j]=true;
                    blocks[x+1][j]*=2;
                    blocks[x][j]=0;
                }
            }
        }
    }

    public void print() {
        for(int i=0;i<n;i++){
            System.out.println(Arrays.toString(blocks[i]));
        }
    }

    public Board clone(){
        return new Board(this);
    }

    public int getMax(){
        int result=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                result=Math.max(result, blocks[i][j]);
            }
        }
        return result;
    }
}