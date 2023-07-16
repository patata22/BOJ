import java.io.BufferedReader;
import java.util.*;

public class Main {
    static int n, m, d;
    static int[] dx = {-1, 1, 0, 0}, dy = {0, 0, -1, 1};
    static boolean[] used;
    static int[][] board;
    static int answer;

    static void simulate(int[] number) {
        int[][] tempboard=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                tempboard[i][j]=board[i][j];
            }
        }
        int temp_answer = 0;
        for (int i = 0; i < n; i++) {
            boolean[][] shot = new boolean[n][m];
            for (int p = 0; p < 3; p++) {
                int[] now = new int[]{n , number[p]};
                boolean[][] visited = new boolean[n][m];
                Queue<int[]> q = new LinkedList();
                q.add(now);
                PriorityQueue<int[]> target = new PriorityQueue<>(new Comparator<int[]>() {
                    @Override
                    public int compare(int[] o1, int[] o2) {
                        int temp = o1[0] - o2[0];
                        if (temp == 0) temp = o1[2] - o2[2];
                        return temp;
                    }
                });
                int t = 0;
                while (!q.isEmpty() && target.isEmpty()&&t<d) {
                    int len = q.size();
                    for (int l = 0; l < len; l++) {
                        int[] temp = q.poll();
                        int x = temp[0], y = temp[1];
                        for (int j = 0; j < 4; j++) {
                            int nx = x + dx[j], ny = y + dy[j];
                            if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                if (tempboard[nx][ny] == 1) target.add(new int[]{t, nx, ny});
                                q.add(new int[]{nx,ny});
                            }
                        }
                    }
                    t += 1;
                }
                if(!target.isEmpty()) {
                    shot[target.peek()[1]][target.peek()[2]] = true;
                }
            }
            for(int a=0;a<n;a++){
                for(int b=0;b<m;b++){
                    if(shot[a][b]){
                        temp_answer+=1;
                        tempboard[a][b]=0;
                    }
                }
            }
            for(int c=n-1;c>0;c--){
                tempboard[c]=tempboard[c-1];
            }
            tempboard[0]=new int[m];
        }
        answer=Math.max(temp_answer,answer);
    }

    static void choice(int start, int count, int[] number) {

        if (count == 3) {
            simulate(number);
            return;
        }
        for (int i = start; i < m; i++) {
            if (!used[i]) {
                used[i] = true;
                number[count] = i;
                choice(i + 1, count + 1, number);
                used[i] = false;
            }
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        d = sc.nextInt();
        board = new int[n][m];
        answer = 0;
        used = new boolean[m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        choice(0,0,new int[3]);
        System.out.println(answer);
    }
}
