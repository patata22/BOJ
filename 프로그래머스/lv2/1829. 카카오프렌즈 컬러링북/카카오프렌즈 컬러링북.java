import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int[] solution(int n, int m, int[][] board) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[] dx = new int[]{-1,1,0,0};
        int[] dy = new int[]{0,0,-1,1};

        boolean[][] visited = new boolean[n][m];
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!visited[i][j]&&board[i][j]!=0){
                    visited[i][j]=true;
                    numberOfArea++;
                    int tempSize = 1;
                    Queue<int[]> q = new ArrayDeque<>();
                    q.add(new int[]{i,j});
                    while(!q.isEmpty()){
                        int x= q.peek()[0];
                        int y= q.poll()[1];
                        for(int k=0;k<4;k++){
                            int nx= x+dx[k];
                            int ny= y+dy[k];
                            if(0<=nx&&nx<n&&0<=ny&&ny<m&&!visited[nx][ny]&&board[nx][ny]==board[i][j]){
                                tempSize++;
                                visited[nx][ny]=true;
                                q.add(new int[]{nx,ny});
                            }
                        }
                    }
                    maxSizeOfOneArea = Math.max(tempSize, maxSizeOfOneArea);
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}